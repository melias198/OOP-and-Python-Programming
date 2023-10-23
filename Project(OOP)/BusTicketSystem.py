class User:
    def __init__(self,username,password):
        self.username = username
        self.password = password

class Bus:
    def __init__(self,coach,driver,arrival,departure,from_des,to):
        self.coach = coach
        self.driver = driver
        self.arrival = arrival
        self.departure = departure
        self.from_des = from_des
        self.to = to
        self.seat = ["Empty" for i in range(1,22)]

class Company:
    total_bus = 10
    bus_list = []

    def add_bus(self):
        bus_no = int(input("Enter Adding Bus Number : "))

        flag = 1
        for val in self.bus_list:
            if bus_no == val['coach']:
                print("Sorry! The Bus Already Added!")
                flag = 0
                break
        if flag:
            bus_driver = input("Enter Bus Driver Name : ")
            bus_arrival = input("Enter Bus Arrival Time : ")
            bus_departue = input("Enter Bus Departure Time : ")
            from_des = input("Enter Bus Start From : ")
            to = input("Enter Bus Destination : ")
            self.new_bus = Bus(bus_no,bus_driver,bus_arrival,bus_departue,from_des,to)
            self.bus_list.append(vars(self.new_bus))
            print("Congrats! Bus Added Successfully.")


class Counter(Company):
    user_list = []

    def buy_ticket(self):
        bus_no = int(input("Enter Your Ticket Buying Bus Number : "))

        for val in self.bus_list:
            if bus_no == val['coach']:
                passenger = input("Enter Your Name : ")
                seat_no = int(input("Enter Your Chosing Seat Number : "))

                if seat_no > 20:
                    print("Sorry! No Seat Available In The Bus!")
                elif val['seat'][seat_no] != "Empty":
                    print("Sorry! The Seat Already Booked")
                else:
                    val['seat'][seat_no] = passenger
            else:
                print("Sorry! No Bus Available.")
    
    def bus_info(self):
        bus_no = int(input("Enter Your Bus Number For Showing Info: "))

        flag = 1
        for val in self.bus_list:
            if bus_no == val['coach']:
                flag = 0
                print(f"{'*'*20} Showing Bus Info {'*'*20}")
                print(f"{' '*10}{'#'*10} Bus Info Of Bus Number {bus_no} {'#'*10}{' '*10}")
                print(f"Bus Number : {bus_no} \t\t\t Driver Name : {val['driver']}")
                print(f"Arrival Time : {val['arrival']} \t\t Departure Time : {val['departure']}")
                print(f"Bus Start From : {val['from_des']} \t Destination : {val['to']}")
                print(f"{' '*10}{'-'*10} Seats Information {'-'*10}{' '*10}")
                a = 1
                for i in range(5):
                    for j in range(2):
                        print(f"{a}. {val['seat'][a]}",end = "\t")
                        a += 1
                    for j in range(2):
                        print(f"{a}. {val['seat'][a]}",end = "\t")
                        a += 1
                    print()
                print('*'*60)
        if flag:
            print("Sorry! No Bus Available.")
            
    
    def create_account(self):
        name = input("Enter Your Username : ")
        password = input("Enter Your Password : ")

        self.new_user = User(name,password)
        self.user_list.append(vars(self.new_user))

    def available_bus(self):
        if len(self.bus_list) == 0:
            print("Sorry! No Bus Available Yet.")
        else:
            print(f"{'*'*20} Available Bus {'*'*20}")
            for bus in self.bus_list:
                print(f"{' '*10}{'#'*10} Bus Info Of Bus Number {bus['coach']} {'#'*10}{' '*10}")
                print(f"Bus Number : {bus['coach']} \t\t\t Driver Name : {bus['driver']}")
                print(f"Arrival Time : {bus['arrival']} \t\t Departure Name : {bus['departure']}")
                print(f"Bus Start From : {bus['from_des']} \t Destination : {bus['to']}")
            print(f"{'*'*50}")



while True:
    Ena = Company()
    Counter_Info = Counter()

    print(f"{'<'}{'-'*10} Welcome To Our Bus Counter System {'-'*10}{'>'}")
    print("1. Create An Account.")
    print("2. Log In.")
    print("3. Exit")

    choice = int(input("Enter Your Choice : "))
    if choice == 3:
        break
    elif choice == 1:
        Counter_Info.create_account()
        print("Congrats! Successfully Account Created.")
    elif choice == 2:
        name = input("Enter Your Username : ")
        password = input("Enter Your Password : ")

        flag = 0
        is_admin = False

        if name == "admin" and password == "123456":
            print(f"{'-'*20} Congrats! Successfylly Admin Logged. {'-'*20}")
            is_admin = True
        
        if is_admin == False:
            for user in Counter_Info.user_list:
                if user['username'] == name and user['password'] == password:
                    print(f"{'-'*20} Congrats! Successfylly Logged. {'-'*20}")
                    flag = 1
            if flag:
                while True:
                    print(f"{' '*10} <- Welcome To Our Ticket Management System -> {' '*10}")
                    print("1. Check Available Bus.")
                    print("2. Show Bus Info.")
                    print("3. Buying Ticket.")
                    print("4. Exit.")
                    choice = int(input("Enter Your Choice : "))
                    if choice == 4:
                        break
                    elif choice == 1:
                        Counter_Info.available_bus()
                    elif choice == 2:
                        Counter_Info.bus_info()
                    elif choice == 3:
                        Counter_Info.buy_ticket()
                        print("Congraltulations! Successfully Bought Ticket.")
                    else:
                        print("Sorry! Invalid Input")
            else:
                print("Sorry! No Account Found.")
        else:
            print(f"{'<'}{'-'*10} Welcome Admin! To Our Managment System {'-'*10}{'>'}")
            print("1. Add Bus.")
            print("2. Check Available Bus.")
            print("3. Check Bus Info.")
            print("4. Exit.")
            choice = int(input("Enter Your Choice : "))
            if choice == 4:
                break
            elif choice == 1:
                Counter_Info.add_bus()
            elif choice == 2:
                Counter_Info.available_bus()
            elif choice == 3:
                Counter_Info.bus_info()
            else:
                print("Sorry! Invalid Input")
    else:
        print("Sorry! Invalid Input.")

        


