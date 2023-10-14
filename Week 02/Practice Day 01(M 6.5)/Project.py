class Product:
    def __init__(self,id,name,price,quantity):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity
        


class Shop:
    def __init__(self):
        self.shop = []

    def add_product(self,id,name,price,quantity):
        product = Product(id,name,price,quantity)
        self.shop.append(product)

    def buy_product(self,id,quantity):
        for product in self.shop:
            if product.id == id:
                if product.quantity >= quantity:
                    return f"Congratulations! {product.name} purchased successfully."
                else:
                    return "Sorry, the product is out of stock."
        return "Product not found in the shop"


My_Cart = Shop()   
My_Cart.add_product(1001,'Bag',480,3) 
My_Cart.add_product(1002,'Pant',430,2) 
My_Cart.add_product(1003,'Shirt',520,5) 

result = My_Cart.buy_product(1001,2)
ans = My_Cart.buy_product(1005,2)
res = My_Cart.buy_product(1003,6)
print(result)
print(ans)
print(res)


         

