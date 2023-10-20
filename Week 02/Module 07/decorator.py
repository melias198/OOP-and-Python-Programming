import math

# it's look like wrapper function

def Calculate(func):
    def inner(*args,**kwargs):
        print('Calculate inner function starting')
        func(*args,**kwargs)
        print('Calculate inner function ended')
    return inner

@Calculate
def Factorial(n):
    result = math.factorial(n)
    print(f'Factorial of number {n} is : {result}')

Factorial(n=5)