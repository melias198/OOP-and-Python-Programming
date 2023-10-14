## What is Inheritance? Explain with examples

Inheritance is a fundamental concept in object-oriented programming (OOP) that allows you to create a new class (called the "subclass" or "child class") by deriving attributes and behaviors from an existing class (called the "superclass" or "parent class"). Inheritance promotes code reuse and hierarchical organization of classes by allowing you to build new classes based on existing ones, inheriting their attributes and methods, and then extending or modifying them as needed.

Here's an explanation of inheritance with examples:
```
class Fruits:
    def __init__(self,name,cal) -> None:
        self.name = name
        self.cal = cal

    def print(self):
        print("Fruits are nature's delicious, colorful, and nutritious gifts for our well-being.")

class Apple(Fruits): #Inheritance
    def __init__(self, name, cal, price) -> None:
        self.price = price
        super().__init__(name, cal)


Kafi = Apple('Apple',220,450)
Kafi.print()
```

## What are Encapsulation and Access Modifiers? Explain with examples

Encapsulation and access modifiers are fundamental concepts in object-oriented programming (OOP) that help control the visibility and accessibility of class members (attributes and methods) within a class. Encapsulation refers to the bundling of data (attributes) and methods that operate on that data into a single unit, often called a class. Access modifiers determine the level of visibility or accessibility of these class members from outside the class. Access modifiers help enforce data hiding and protect the internal state of objects.
here are typically three main access modifiers in most OOP languages:

- Public: Members with public access modifiers are accessible from anywhere, both within and outside the class. There are no restrictions on access.
- Protected: Members with protected access modifiers are accessible within the class and its subclasses. Subclasses can access protected members, but external code cannot.
- Private: Members with private access modifiers are accessible only within the class in which they are declared. They are not accessible from outside the class, even from subclasses.

Example of Encapsulation and Access Modifiers in Python:
```
class Bank:
    def __init__(self,account_holdar,account_type) -> None:
        self.__balance = 10000000 #Private attributes
        self._account_holdar = account_holdar #Protected attributes
        self.account_type = account_type #Public attributes

    def deposit(self,amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance
    
    
Mahi = Bank('Mahi','Savings')
# print(Mahi.__balance) Can't access private attributes
print(Mahi._account_holdar) #Protected attributes can access
print(Mahi.account_type) #Public attributes can access

Mahi.deposit(5000)
print(Mahi.get_balance())

print(Mahi._Bank__balance) #We can access private attributes using this
```