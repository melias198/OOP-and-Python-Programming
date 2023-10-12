class Shop:
    def __init__(self):
        self.cart = []

    def add_cart(self,item,price,quantity):
        product = {'Item': item, 'Price': price, 'Quantity': quantity}
        self.cart.append(product)

    def check_out(self,amount):
        total = 0
        for item in self.cart:
            total += item['Price']*item['Quantity']
        print("Total Payable:",total)
        if total>amount:
            print("Payable Due:",total-amount)
        else:
            print("Take Extra:",amount-total)

Rahi = Shop()
Rahi.add_cart("Apple",380,2)
Rahi.add_cart("Orange",430,3)
Rahi.add_cart("Graps",450,1)

Rahi.check_out(3000)