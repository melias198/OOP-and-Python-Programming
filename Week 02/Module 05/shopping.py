class Shopping:
    def __init__(self):
        self.cart = []

    def add_to_cart(self,item):
        self.cart.append(item)
    
    def remove_from_cart(self,item):
        if item in self.cart:
            self.cart.remove(item)


Mahi = Shopping()
Mahi.add_to_cart('Bag')
Mahi.add_to_cart('Perfume')
Mahi.add_to_cart('Lipstick')
print(Mahi.cart)
Mahi.remove_from_cart('Bag')
print(Mahi.cart)

Sahid = Shopping()
Sahid.add_to_cart('Shirt')
Sahid.add_to_cart('Pant')
Sahid.add_to_cart('Shoes')
Sahid.add_to_cart('T-Shirt')
print(Sahid.cart)
