class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Duck(Animal):
    def speak(self):
        return "Quack!"


dog = Dog()
cat = Cat()
duck = Duck()

animals = [dog,cat,duck]

for animal in animals:
    print(animal.speak())