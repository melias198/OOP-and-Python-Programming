class User:
    def __init__(self,name,phone,email,password):
        self.name = name
        self.phone = phone
        self.email = email
        self.password = password


class Seller(User):
    def __init__(self, name, phone, email, password,verification):
        self.verification = verification
        super().__init__(name, phone, email, password)


class Product:
    def __init__(self,name,catagory,price,quantity,status):
        self.name = name
        self.catagory = catagory
        self.price = price
        self.quantity = quantity
        self.status = status


class Shop:
    product_list = []
    user_list = []
    seller_list = []

    def add_product(self):
        product = input("Enter Your Product Name : ")
        catagory = input("Enter Your Product Catagory : ")
        price = int(input("Enter Your Product Price : "))
        quantity = int(input("Enter Your Product Quantity : "))
        status = None

        if quantity>0:
            status = 'stock'
        else:
            status = 'out'
        
        self.new_product = Product(product,catagory,price,quantity,status)
        self.product_list.append(vars(self.new_product))


    def buy_product(self):
        name = input("Enter Your Buying Product Name : ")
        catagory = input("Enter Your Buying Product Catagory : ")

        flag = 1
        for val in self.product_list:
            if name == val['name'] and catagory == val['catagory']:
                flag = 0
                print(f"Your Choosing Product Available Quantity : {val['quantity']}")
                quantity = int(input("Enter Your Buying Product Quantity : "))
                if quantity<=val['quantity']:
                    val['quantity'] -= quantity
                    if val['quantity'] == 0:
                        val['status'] = 'out'
                    print(f"Your Total Price is : {val['price']*quantity}, Please Select Payment Method:")
                    print("1. Online Payment")
                    print("2. Cash On Delivary")
                    choice = int(input("Enter Your Choice : "))
                    if choice == 1:
                        print("Thank You! Let's Make Your Day Happy.")
                    elif choice == 2:
                        print("Thank You! See You Soon.")
                    else:
                        print("Invalid Choice")
                else:
                    print("Your Product Quantity Out of stock")
        if flag:
            print("No Found Your Product")


    
    def show_product(self):
        print("|------------Showing Our Stock Product------------|")
        for val in self.product_list:
            if val['status'] == 'stock':
                print(f"Product Name : {val['name']}\nProduct Price : {val['price']}\nProduct Catagory : {val['catagory']}\nProduct Quantity : {val['quantity']}\nStatus : {val['status']}")
                print("------------------------------")




    def create_account_user(self):
        name = input("Enter Your Name : ")
        phone = input("Enter Your Phone Number : ")
        email = input("Enter Your Email : ")
        password = input("Enter Your Password : ")

        self.new_user = User(name,phone,email,password)
        self.user_list.append(vars(self.new_user))
    
    def create_account_seller(self):
        name = input("Enter Your Name : ")
        phone = input("Enter Your Phone Number : ")
        email = input("Enter Your Email : ")
        password = input("Enter Your Password : ")
        verify = input("Enter Your Verification Code : ")

        self.new_seller = Seller(name,phone,email,password,verify)
        self.seller_list.append(vars(self.new_seller))

    
while True:
    Online_Shop = Shop()
    print("<---------Welcome To Our Online Shop.--------->")
    print("1. Sign Up")
    print("2. Login")
    print("3. Quit")
    choice = int(input("Enter Your Choice : "))

    if choice == 3:
        break
    elif choice == 1:
        while True:
            print("1. Sign Up as Seller")
            print("2. Sign Up as User")
            print("3. Back ")
            a = int(input("Enter Your Choice : "))
            if a == 3:
                break
            elif a == 1:
                Online_Shop.create_account_seller()
                print("Successfully Seller Account Created, Please Login First")
            elif a == 2:
                Online_Shop.create_account_user()
                print("Successfully User Account Created, Please Login First")
            else:
                print("Invalid Choice")
    elif choice == 2:
        while True:
            print("1. Login as Seller")
            print("2. Login as User")
            print("3. Back")
            b = int(input("Enter Your Choice : "))
            if b == 3:
                break
            elif b == 1:
                email = input("Enter Your Email or Phone : ")
                password = input("Enter Your Password : ")

                flag = 1
                for seller in Online_Shop.seller_list:
                    if seller['email'] == email or seller['phone'] == email:
                        if seller['password'] == password:
                            flag = 0
                            print("...............Successfully Seller Login............")
                            while True:
                                print("1. Add Product")
                                print("2. Show Product")
                                print("3. Back")

                                c = int(input("Enter Your Choice : "))
                                if c == 3:
                                    break
                                elif c == 1:
                                    Online_Shop.add_product()
                                    print("Succesfully Added Product")
                                elif c == 2:
                                    Online_Shop.show_product()
                                else:
                                    print("Invalid Choice")
                if flag:
                    print("No Seller Found")

            elif b == 2:
                email = input("Enter Your Email or Phone : ")
                password = input("Enter Your Password : ")

                flag = 1
                for user in Online_Shop.user_list:
                    if user['email'] == email or user['phone'] == email:
                        if user['password'] == password:
                            flag = 0
                            print("...........Successfully User Login.............")
                            while True:
                                print("1. Buy Product")
                                print("2. Show Product")
                                print("3. Back")
                                d = int(input("Enter Your Choice : "))
                                if d == 3:
                                    break
                                elif d == 1:
                                    Online_Shop.buy_product()
                                elif d == 2:
                                    Online_Shop.show_product()
                                else:
                                    print("Invalid Choice")
                if flag:
                    print("No User Found")
            else:
                print("Invalid Choice")

    else:
        print("Invalid Choice")


            