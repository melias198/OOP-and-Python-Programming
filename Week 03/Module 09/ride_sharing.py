class User:
    user_list = []
    def __init__(self,username,email,password):
        self.username = username
        self.email = email
        self.password = password
    

    def register(self):
        User.user_list.append(vars(self))
        print("User Registration successful!")
    

    def login(self,email,password):
        flag = 1
        for user in self.user_list:
            if user['email'] == email and user['password'] == password:
                flag = 0
                print("User Login Successful!")

        if flag:
            print("User Login Failed!")


class Driver(User):
    driver_list = []
    def __init__(self, username, email, password):
        super().__init__(username, email, password)


    def register(self):
        Driver.driver_list.append(vars(self))
        print("Driver Registration successful!")


    def login(self,email,password):
        flag = 1
        for driver in self.driver_list:
            if driver['email'] == email and driver['password'] == password:
                flag = 0
                print("Driver Login Successful!")
        
        if flag:
            print("Admin Login Failed!")


class Passenger(User):
    def __init__(self, username, email, password,payment_info,ride_history,preferences):
        super().__init__(username, email, password)
        self.payment_info = payment_info
        self.ride_history = ride_history
        self.preferences = preferences
    

    def view_ride_history(self):
        print(f"Ride history for passenger {self.username}:")
        for ride in self.ride_history:
            print(ride)


class Ride:
    def __init__(self,pickup_location,dropoff_location,driver,passenger):
        self.pickup_location = pickup_location
        self.dropoff_location = dropoff_location
        self.driver = driver
        self.passenger = passenger

        self.passenger.ride_history.append(f"Dhaka to Ctg Ride with driver {self.driver.username}")

    
    def calculate_fare(self):
        return 100


    def display_ride_details(self):
        print(f"Ride Details:")
        print(f"Pickup Location: {self.pickup_location}")
        print(f"Drop-off Location: {self.dropoff_location}")
        print(f"Driver: {self.driver.username}")
        print(f"Passenger: {self.passenger.username}")
        print(f"Fare: ${self.calculate_fare()}")
        
    


passenger = Passenger('Elias','elias@gmail.com','1234','cash',[],'bike')
passenger.register()
driver = Driver('Karim','karim@gmail.com','4567')
driver.register()

print(passenger.user_list)
print(driver.driver_list)

new_ride = Ride('Dhaka','Ctg',driver,passenger)
new_ride.display_ride_details()
new_ride.calculate_fare()

passenger.view_ride_history()