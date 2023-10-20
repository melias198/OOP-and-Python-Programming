## Write what are getter and setter with proper examples

#### Gretter:
A getter method is used to retrieve the value of an attribute. It provides read-only access to the attribute and often starts with the word "get."

#### Setter:
A setter method is used to modify the value of an attribute. It provides write access to the attribute and often starts with the word "set."

Example:
```
class Bank:
    def __init__(self,name,amount,user):
        self.name = name
        self.__amount = amount
        self.__user = user

    # getter,means read only
    @property #using this Amount would be an attribute not method
    def Amount(self):
        return self.__amount
    
    @Amount.setter #setter 
    def Add_Amount(self,value):
        self.__amount += value



IBBL = Bank('IBBL',1000,300)
print(IBBL.Amount)
IBBL.Add_Amount = 5000
print(IBBL.Amount)
```
