import math

class Calculation:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    
    def sum(self):
        return self.a+self.b+self.c
    
    def factorial(self):
        return math.factorial(self.b)
    
Numbers = Calculation(2,5,3)
print(Numbers.sum())
print(Numbers.factorial())