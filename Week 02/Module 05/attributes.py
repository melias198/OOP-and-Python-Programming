class Shop:
    cart = [] #Class Attributes

    def __init__(self):
        pass

    def add_cart(self,item):
        self.cart.append(item)

Mahi = Shop()
Mahi.add_cart("Apple")
Mahi.add_cart("Orange")
Mahi.add_cart("Lemon")

print("Mahi's Cart:",Mahi.cart)

Sahi = Shop()
Sahi.add_cart("Bag")
Sahi.add_cart("Shoes")
Sahi.add_cart("T-Shirt")

print("Sahi's Cart:",Sahi.cart)

print()

class Shop2:
    def __init__(self):
        self.cart = [] #Instance Attributes

    def add_cart(self,item):
        self.cart.append(item)

Mahi = Shop2()
Mahi.add_cart("Apple")
Mahi.add_cart("Orange")
Mahi.add_cart("Lemon")

print("Mahi's Cart:",Mahi.cart)

Sahi = Shop2()
Sahi.add_cart("Bag")
Sahi.add_cart("Shoes")
Sahi.add_cart("T-Shirt")

print("Sahi's Cart:",Sahi.cart)