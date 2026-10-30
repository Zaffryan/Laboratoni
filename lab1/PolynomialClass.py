class Polynomial():
    def __init__(self, *coefficients):
        if (len(coefficients) == 1 and isinstance(coefficients[0], (list,tuple))):
            start_coef = list(coefficients[0])
            self.coefficients = self.delete_nulls(start_coef)
        elif (len(coefficients) == 1 and isinstance(coefficients[0], dict)):
            dict_coef = coefficients[0]
            if (len(dict_coef) == 0):
                start_coef = [0]
            else:
                mkey = max(dict_coef)
                start_coef = [0]*(mkey+1)
                for st, co in dict_coef.items():
                    start_coef[st] = co
            self.coefficients = self.delete_nulls(start_coef)
        elif (len(coefficients) == 1 and isinstance(coefficients[0], Polynomial)):
            self.coefficients = list(coefficients[0].coefficients)
        else:
            start_coef = list(coefficients)              
            self.coefficients = self.delete_nulls(start_coef)

    def delete_nulls(self, start_coef):
        while (len(start_coef) > 1 and start_coef[-1] == 0):
            start_coef.pop()
        if len(start_coef) == 0:
            start_coef = [0]
        return start_coef
    
    def __repr__(self):
        return f'Polynomial {self.coefficients}'

    def __str__(self):
        if (self.coefficients == [0]):
            return '0'
        pol = ''
        for i in range(len(self.coefficients) -1, -1, -1):
            if (self.coefficients[i] != 0):
                if (i == len(self.coefficients)-1):
                    if (i == 0):
                        pol += f'{self.coefficients[i]}'
                    elif (self.coefficients[i] == 1):
                        pol += f'x^{i}' if i != 1 else 'x'
                    elif (self.coefficients[i] == -1):
                        pol += f'-x^{i}' if i != 1 else '-x'
                    elif (i == 1):
                        pol += f'{self.coefficients[i]}x'
                    else:
                        pol += f'{self.coefficients[i]}x^{i}'    
                else:
                    if (i > 0):
                        if (self.coefficients[i] > 0):
                            if (self.coefficients[i] == 1):
                                pol += f' + x^{i}' if i != 1 else ' + x'
                            elif (i == 1):
                                pol += f' + {abs(self.coefficients[i])}x'
                            else:
                                pol += f' + {abs(self.coefficients[i])}x^{i}'    
                        else:
                            if (self.coefficients[i] == -1):
                                pol += f' - x^{i}' if i != 1 else ' - x'
                            elif (i == 1):
                                pol += f' - {abs(self.coefficients[i])}x'
                            else:
                                pol += f' - {abs(self.coefficients[i])}x^{i}'
                    else:
                        pol += f' + {abs(self.coefficients[i])}' if self.coefficients[i] > 0 else f' - {abs(self.coefficients[i])}'
        return pol  

    def __eq__(self, other):
        if isinstance(other, Polynomial):
            return self.coefficients == other.coefficients
        if isinstance(other, int):
            return self.coefficients == [other]       

    def __add__(self, other):
        if isinstance(other, Polynomial):
            pol = list(self.coefficients)
            oth = list(other.coefficients)
            maxlen = max(len(pol), len(oth))
            res = [0] * maxlen
            if (len(pol) < maxlen):
                for i in range(maxlen-len(pol)):
                    pol.append(0)
            if (len(oth) < maxlen):
                for i in range(maxlen-len(oth)):
                    oth.append(0)
            for i in range(maxlen):
                res[i] = pol[i] + oth[i]
            return Polynomial(res)
        if isinstance(other, int):
            pol = list(self.coefficients)
            pol[0] += other
            return Polynomial(pol)

    def __radd__(self, other):
        return self + other

    def __neg__(self):
        pol = list(self.coefficients)
        for i in range (len(pol)):
            pol[i] = -pol[i]
        return Polynomial(pol)

    def __sub__(self, other):
        if isinstance(other, Polynomial):
            pol = list(self.coefficients)
            oth = list(other.coefficients)
            maxlen = max(len(pol), len(oth))
            res = [0] * maxlen
            if (len(pol) < maxlen):
                for i in range(maxlen-len(pol)):
                    pol.append(0)
            if (len(oth) < maxlen):
                for i in range(maxlen-len(oth)):
                    oth.append(0)
            for i in range(maxlen):
                res[i] = pol[i] - oth[i]
            return Polynomial(res)
        if isinstance(other, int):
            pol = list(self.coefficients)
            pol[0] -= other
            return Polynomial(pol)

    def __rsub__(self, other):
        return (-self) + other

    def degree(self):
        return len(self.coefficients) -1

    def der(self, d=1):
        pol = list(self.coefficients)
        for i in range(d):
            if len(pol) == 1:
                return Polynomial([0])
            res = []
            for j in range(1, len(pol)):
                res.append(pol[j]*j)
            pol = res
        return Polynomial(pol)

    def __mul__(self, other):
        if isinstance(other, Polynomial):
            pol = list(self.coefficients)
            oth = list(other.coefficients)
            res = [0] * (len(pol) + len(oth) -1)
            for i in range(len(pol)):
                for j in range(len(oth)):
                    res[i+j] += pol[i] * oth[j]
            return Polynomial(res)
        if isinstance(other, int):
            pol = list(self.coefficients)
            for i in range(len(pol)):
                pol[i]*=other
            return Polynomial(pol)

    def __rmul__(self, other):
        return self * other

    def __iter__(self):
        self.iterator = 0
        return self

    def __next__(self):
        if self.iterator >= len(self.coefficients):
            raise StopIteration
        res = (self.iterator, self.coefficients[self.iterator])
        self.iterator += 1
        return res





