class Fruits:
    def __init__(self,name,cal) -> None:
        self.name = name
        self.cal = cal

    def print(self):
        print("Fruits are nature's delicious, colorful, and nutritious gifts for our well-being.")

class Apple(Fruits):
    def __init__(self, name, cal, price) -> None:
        self.price = price
        super().__init__(name, cal)


Kafi = Apple('Apple',220,450)
Kafi.print()