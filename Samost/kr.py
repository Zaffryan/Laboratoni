#1 декортаор время выполениния йункции
#2 генератор бескончной последовательности

import time
def timer_decorator(fn):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        ret_val = fn(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"Функция выполнена, время выполнения функции: {end_time-start_time}")
        return ret_val
    return wrapper

@timer_decorator
def summa(n):
    res = 0
    for i in range(n):
        res+=i
    return res
    

summa(100000000)

def inf_gen(val):
    while True:
        yield val
        val+=1
a = inf_gen(5)
print("бесконечный генератор")
for i in range(10):
    print(next(a))

def gen_Fibonachi():
    a = 0
    b = 1
    c = a+b
    while True:
        yield a
        a = b
        b = c
        c = a+b
print("генератор фибоначчи")
a = gen_Fibonachi()
for i in range(10):
    print(next(a)) 

