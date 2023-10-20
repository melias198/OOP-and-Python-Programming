# Composition provides "has a" relation

class Engine:
    pass

# Car has a Engine
class Car:
    def __init__(self):
        self.engine = Engine()



class CPU:
    pass
# Computer has cpu
class Computer:
    def __init__(self):
        self.cpu = CPU()