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


#without using property getter setter would be method not attribute
class MyClass:
    def __init__(self):
        self._my_attribute = None

    def get_my_attribute(self):
        return self._my_attribute

    def set_my_attribute(self, value):
        if value < 0:
            raise ValueError("Value must be non-negative")
        self._my_attribute = value

# Usage
obj = MyClass()
obj.set_my_attribute(42)  # Calls the setter method
print(obj.get_my_attribute())  # Calls the getter method
