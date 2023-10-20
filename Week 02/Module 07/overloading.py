class Person:
    def __init__(self,name,age,weight,height):
        self.name =  name
        self.age = age
        self.weight = weight
        self.height = height

    

class Cricketer(Person):
    def __init__(self, name, age, weight, height,team):
        self.team = team
        super().__init__(name, age, weight, height)

    # overloading
    def __add__(self,other):
        return self.age + other.age
    
    def __lt__(self,other):
        return self.age < other.age
    



Sakib = Cricketer('Sakib Al Hasan',35,80,165,'Bangladesh')
Musfiqe = Cricketer('Musfiqur Rahim',36,60,150,'Bangladesh')
Shanto = Cricketer('Nazmul Hossain Shanto',23,75,163,'Bangladesh')
Hridoy = Cricketer('Tawhid Hridoy',22,70,164,'Bangladesh')

Result = Sakib + Musfiqe
print(Result)

Youngest = min([Sakib,Musfiqe,Shanto,Hridoy])
print(Youngest.name)