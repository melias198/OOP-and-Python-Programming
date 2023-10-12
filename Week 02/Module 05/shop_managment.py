class Item:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class ShoppingCart:
    prices = 0
    
    def __init__(self):
        self.cart = []
    
    def add_item(self,item,quantity):
        if quantity <= item.quantity:
            self.cart.append((item, quantity))
            item.quantity -= quantity
            print(f'Successfully added {item.name} {quantity}pcs in your cart.')
        else:
            print(f'Not enough {item.name} in shop.')
    
    def remove_cart(self,item,quantity):
        for cart_item, cart_quantity in self.cart:
            if cart_item == item:
                if quantity <= cart_quantity:
                    cart_item.quantity += quantity
                    self.cart.remove((cart_item, cart_quantity))
                    print(f"{item.name}(s) removed from your cart.")
                else:
                    print(f"Sorry, you have only {cart_quantity} {item.name}(s) in your cart.")

    def view_cart(self):
        if not self.cart:
            print("Your cart is empty.")
        else:
            print("Shopping Cart:")
            total_price = 0
            for item, quantity in self.cart:
                item_price = item.price * quantity
                print(f"{item.name}: {quantity} x {item.price} = {item_price}")
                total_price += item_price
            print(f"Total Payment: {total_price}")    

    
        

Item1 = Item('Shirt',450,2)
Item2 = Item('Pant',500,5)

Mahi = ShoppingCart()
Mahi.add_item(Item1,2)
Mahi.add_item(Item2,3)

Mahi.view_cart()

Mahi.remove_cart(Item2,1)

Mahi.view_cart()


