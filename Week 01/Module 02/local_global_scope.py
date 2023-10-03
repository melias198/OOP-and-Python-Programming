balance = 5000

def shopping(item,price):
    # I can access global variable without using global keyword but can't modify
    global balance #If I modify global variable then used to global keyword
    balance-=price
    print(item,balance)

shopping("Apple",1000)
print(balance)