def f(a):
    if isinstance(a,list):
        r=[]
        for i in a:
            i = f(i)
            if i not in ('',[],{},()):
                r.append(i)
        return r
    if isinstance(a,set):
        r=set()
        for i in a:
            i=f(i)
            if i not in ('',[],{},()):
                r.add(i)
        return r
    if isinstance(a,str):
        if a != '':
            return a
    if isinstance(a,dict):
            r={}
            for i in a:
                if i not in ('',[],{},()):
                    r[i] = f(a[i])
            return r
    return a
    


s = [[[],['2']],'2','',"",(2,1), {'':2, "a": 4}, [[],()], ((),[])]
x = {"":[], "g" : [2,()]}

print(f(s), f(x), sep = "\n")

