## Question: Write what is meant by operator overloading and method overriding with examples.

### Overloading:
Operator overloading is a concept in object-oriented programming that allows you to define how operators, such as +, -, *, /, etc., work with objects of custom classes. It enables you to give specific meaning to these operators when applied to instances of your own classes. By overloading operators, you can make your code more intuitive and readable.
For example, you can define the behavior of the + operator for two objects of a custom class:
```
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

point1 = Point(1, 2)
point2 = Point(3, 4)
result = point1 + point2  # This uses the overloaded + operator
print(result.x, result.y)  # Output: 4 6

```

### Overriding:
Method overriding is a feature in object-oriented programming that allows a subclass to provide a specific implementation for a method that is already defined in its superclass. The overridden method in the subclass has the same name, return type, and parameters as the method in the superclass, but it provides a different behavior.
For example:
```
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

animal = Animal()
animal.speak()  # Output: "Animal speaks"

dog = Dog()
dog.speak()  # Output: "Dog barks"
```
