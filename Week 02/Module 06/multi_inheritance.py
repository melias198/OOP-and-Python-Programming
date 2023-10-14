class Vehicle:
    def __init__(self,name,price) -> None:
        self.name = name 
        self.price = price


class Truck(Vehicle):
    def __init__(self, name, price,weight) -> None:
        self.weight = weight
        super().__init__(name, price)


class Mini_Truck(Truck):
    def __init__(self, name, price, weight,chesis) -> None:
        self.chesis = chesis
        super().__init__(name, price, weight)

class Pick_Up(Mini_Truck):
    def __init__(self, name, price, weight, chesis,engine) -> None:
        self.engine = engine
        super().__init__(name, price, weight, chesis)

    def __repr__(self) -> str:
        return f'{self.name} PickUp was bought {self.price} taka. The PickUp capacity is {self.weight},Engine mady by {self.engine} and Chesis number is {self.chesis}'


PickUp = Pick_Up('Ma Babar Dowa',800000,'300 kg','BD-94367234','China')
print(PickUp)
