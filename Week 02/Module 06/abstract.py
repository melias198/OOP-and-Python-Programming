from abc import ABC, abstractmethod
#An abstract class is a class that can have both concrete (implemented) methods and abstract (unimplemented) methods.

class Animal(ABC):
    @abstractmethod #Ensuring all derive class have a move method
    def move(self): #abstract method -> unimplement method
        pass
    @abstractmethod
    def speak(self): #Concrete method -> implement method
        print("Animal can speak")

    

class Human(Animal):
    def move(self):
        print("Human can walk and run")

    def speak(self):
        print('Human speak by sounds')


class Dog(Animal):
    def move(self):
        print("Dog can bark")

    def speak(self):
        print('Dog speak by barking')

H = Human()
H.move()
H.speak()

D = Dog()
D.move()
D.speak()

