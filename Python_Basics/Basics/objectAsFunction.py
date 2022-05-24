import re
from wsgiref.util import request_uri


def sum(a, b):
    return a+b
def mul(a, b):
    return a*b


## Assinging functions to a variable and Using it
sum_func_var = sum

mul_func_var = mul

print(sum_func_var(10,20))

print(mul_func_var(10,20))


#pass function as parametere

def SumMul(a,b):
    #here b is a function
    return b(a,a)+b(a,a)

SumMul(10,sum_func_var)


##Function as part of another object


def add(a,b):
    return a+b

function_list = [add(1,2),add(3,4),add(5,6)]

for i,func in enumerate(function_list):
    #print(i)
    print(func)