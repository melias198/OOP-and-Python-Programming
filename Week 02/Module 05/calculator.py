class Calculator:
    def __init__(self,a,char,b):
        self.a=a
        self.char=char
        self.b=b
    
    def Calculation(self):
        if self.char=='+':
            return self.a+self.b
        elif self.char=='-':
            return self.a-self.b
        elif self.char=='*':
            return self.a*self.b
        elif self.char=='/':
            if self.b==0:
                return 'You Can\'t divide by Zero'
            return self.a/self.b
        else:
            return 'Invalid Operator'
        
add = Calculator(5,'+',12)
ans = add.Calculation()
print(ans)

