from abc import ABC, abstractmethod
# An interface is a class that consists entirely of abstract (unimplemented) methods, without any concrete methods or attributes.

class Shape(ABC):
    @abstractmethod
    def sides(self):
        pass

class Area(ABC):
    @abstractmethod
    def area(self):
        pass

class Triangle(Shape,Area):
    def sides(self):
        print("Triangle has three sides")

    def area(self):
        print("Triangle area is 0.5*base*height")

Tri_Angle = Triangle()
Tri_Angle.sides()
Tri_Angle.area()

