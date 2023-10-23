def register():
    username = input("Enter a username : ")
    password = input("Enter a password : ")

    if is_username_taken(username):
        print("Username is already taken. Please choose another one.")
    else:
        with open("users.txt", "a") as file:
            file.write(f"{username}:{password}\n")
    
        print("Registration successful!")


def is_username_taken(username):
    with open("users.txt", "r") as file:
        for line in file:
            stored_username, _ = line.strip().split(":")
            if username == stored_username:
                return True
    return False

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    with open("users.txt", "r") as file:
        lines = file.readlines()

    for line in lines:
        stored_username, stored_password = line.strip().split(":")
        if username == stored_username and password == stored_password:
            print("Login successful!")
            return

    print("Login failed. Please check your username and password.")

while True:
    print("<----Welcome to the Login and Registration System---->")
    print("1. Register")
    print("2. Login")
    print("3. Quit")
    choice = int(input("Enter your choice : "))

    if choice == 1:
        register()
    elif choice == 2:
        login()
    elif choice == 3:
        break
    else:
        print("Invalid choice. Please try again.")
