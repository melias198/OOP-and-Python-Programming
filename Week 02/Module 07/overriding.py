class Person:
    def __init__(self,name,age,weight,height):
        self.name =  name
        self.age = age
        self.weight = weight
        self.height = height

    def eat(self):
        print('Person has a list meal.')

class Cricketer(Person):
    def __init__(self, name, age, weight, height,team):
        self.team = team
        super().__init__(name, age, weight, height)

    # overriding
    def eat(self):
        print('Cricketer has special meal list for their fitness concern.')


Sakib = Cricketer('Sakib Al Hasan',35,80,165,'Bangladesh')
Sakib.eat()