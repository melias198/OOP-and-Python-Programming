class User:
    user_list = []
    def __init__(self,name,email,password,type):
        self.name = name
        self.email = email
        self.password = password
        self.type = type
        self.user_cart = []

        User.user_list.append(vars(self))


class Admin:
    admin_list = []
    def __init__(self,name,email,password,type):
        self.name = name
        self.email = email
        self.password = password
        self.type = type

        Admin.admin_list.append(vars(self))


class Book:
    def __init__(self,book_name,author,price,page,genre,quantity):
        self.book_name = book_name
        self.author = author
        self.price = price
        self.page = page
        self.genre = genre
        self.quantity = quantity
        

class Library:
    book_list = []
    history_list = []

    def add_book(self):
        name = input("\nEnter book name : ")
        author = input("Enter author name : ")
        price = int(input("Enter book price : "))
        page = int(input("Enter page numbers : "))
        genre = input("Enter book genre : ")
        quantity = int(input("Enter book quantity : "))

        self.book = Book(name,author,price,page,genre,quantity)
        self.book_list.append(vars(self.book))
    

    def available_books(self):
        sl = 1
        print("\n<>------Available books of Our Library------<>")
        for book in self.book_list:
            if book['quantity'] > 0:
                print(f"{sl}. {book['book_name']}")
                sl += 1
            
        print("<-------------------------------------------->\n")


    def serach_book(self):
        name = input("\nEnter your searching book name : ")

        flag = 1
        for book in self.book_list:
            if name == book['book_name']:
                flag = 0
                print("\n----------Book details----------")
                print(f"Name : {book['book_name']} \t\t Page : {book['page']}")
                print(f"Author : {book['author']} \t\t Price : {book['price']}")
                print(f"Genre : {book['genre']} \t\t Quatity : {book['quantity']}")
                print("--------------------------------")
        if flag:
            print("\nNot found. May be not in library or search corrected name.")
            

    
    def borrow_book(self,user):
        name = input("\nEnter your borrowing book name : ")

        flag = 1
        for book in self.book_list:
            if name == book['book_name'] and book['quantity'] > 0:
                flag = 0
                user['user_cart'].append(f"{name}")
                book['quantity'] -= 1
                self.history_list.append(f"{user['name']}, Borrowed {name} Book")
                print(f"\nSuccessfully brrowed {name} from library")
        if flag:
            print("\nNo found, try again")

    def return_book(self,user):
        print("\n........Your borrowing books........\n")
        sl = 1
        for book in user['user_cart']:
            print(f"{sl}. {book}")
            sl += 1
        
        choice = int(input("\nEnter serial number to return : "))
        if choice <= len(user['user_cart']):
            b = user['user_cart'].pop(choice-1)
            self.history_list.append(f"{user['name']}, Returned {b} Book")
            for bk in self.book_list:
                if b == bk['book_name']:
                    bk['quantity'] += 1
            print(f"\nSuccessfully return {b} to library")
        else:
            print("\nInvalid choice")


    def my_library(self,user):
        print(f"\n<>------Hi {user['name']}, your library------<>\n")
        sl = 1
        for book in user['user_cart']:
            print(f"{sl}. {book}")
            sl += 1
        print("<------------------------------------->")

    
    def library_history(self):
        print("\n<-------Library history------->")
        sl = 1
        for history in self.history_list:
            print(f"{sl}. {history}")
            sl += 1
        print("<------------------------------>\n")




library = Library()

while True:
    print("\n<>-----Wellcome to our Library Management System-----<>\n")
    print("1. User")
    print("2. Admin")
    print("3. Quit")

    choice = int(input("\nEnter your choice : "))
    if choice == 3:
        break
    elif choice == 1:
        while True:
            print("\n<------Welcome to the user interface------>\n")
            print("1. Create account")
            print("2. Login")
            print("3. Back")

            a = int(input("\nEnter your choice : "))
            if a == 3:
                break
            elif a == 1:
                name = input("\nEnter your name : ")
                email = input("Enter your email : ")
                password = input("Enter your password : ")
                user_ac = User(name,email,password,'user')
                print("\nSuccessfully user account created")
            elif a == 2:
                email = input("\nEnter your email : ")
                password = input("Enter your password : ")

                flag = 1
                for user in user_ac.user_list:
                    if email == user['email'] and password == user['password']:
                        flag = 0
                        while True:
                            print(f"\n<^>-----Wellcome {user['name']}, to our library-----<^>\n")
                            print("1. Check Available Books")
                            print("2. Search Book")
                            print("3. Borrow Book")
                            print("4. My Library")
                            print("5. Return Book")
                            print("6. Logout")

                            b = int(input("\nEnter your choice : "))
                            if b == 6:
                                break
                            elif b == 1:
                                library.available_books()
                            elif b == 2:
                                library.serach_book()
                            elif b == 3:
                                library.borrow_book(user)
                            elif b == 4:
                                library.my_library(user)
                            elif b == 5:
                                library.return_book(user)
                            else:
                                print("Invalid choice.")
                if flag:
                    print("No user found")
            else:
                print("Invalid choice.")

    elif choice == 2:
        while True:
            print("\n<------Welcome to the admin interface------>\n")
            print("1. Create account")
            print("2. Login")
            print("3. Back\n")

            c = int(input("Enter your choice : "))
            if c == 3:
                break
            elif c == 1:
                name = input("\nEnter your name : ")
                email = input("Enter your email : ")
                password = input("Enter your password : ")
                admin_ac = Admin(name,email,password,'user')
                print("\nSuccessfully admin account created")
            elif c == 2:
                email = input("Enter your email : ")
                password = input("Enter your password : ")

                flag = 1
                for admin in admin_ac.admin_list:
                    if admin['email'] == email and admin['password']:
                        flag = 0
                        while True:
                            print(f"\n<^>-----Wellcome {admin['name']}, to our library-----<^>\n")
                            print("1. Check Available Books")
                            print("2. Add Book")
                            print("3. Library History")
                            print("4. Logout")

                            d = int(input("\nEnter your choice : "))
                            if d == 4:
                                break
                            elif d == 1:
                                library.available_books()
                            elif d == 2:
                                library.add_book()
                                print("\nSuccessfully added new book.")
                            elif d == 3:
                                library.library_history()
                            else:
                                print("Invalid choice.")
            else:
                print("Invalid choice.")
    else:
        print("Invalid choice.")




    
    






        