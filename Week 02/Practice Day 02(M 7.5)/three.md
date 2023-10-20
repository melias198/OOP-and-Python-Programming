## Write down 4 differences between the class method and static method with proper examples.

The difference between the Class method and the static method is:

- A class method takes self as the first parameter while a static method needs no specific parameters.
- A class method can access or modify the class state while a static method can’t access or modify it.
- In general, static methods know nothing about the class state. They are utility-type methods that take some parameters and work upon those parameters. On the other hand class methods must have class as a parameter.
- We use `@classmethod` decorator in python to create a class method and we use `@staticmethod` decorator to create a static method in python.

Stactic Method:
```
class Math:
    @staticmethod
    def add(a,b):
        return a+b
    
Add = Math.add(4,6)
print(Add)
```

Class Method:
```
class MyClass:
    Name = 'Karim'
    def __init__(self,name):
        self.name = name

    @classmethod
    def MyInstance(self,address):
        self.address = address

MyClass.MyInstance('Dhaka')
MyClass.address = 'Pekua'
print(MyClass.address)
```
