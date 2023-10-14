class Bank:
    def __init__(self,account_holdar,account_type) -> None:
        self.__balance = 10000000 #Private attributes
        self._account_holdar = account_holdar #Protected attributes
        self.account_type = account_type #Public attributes

    def deposit(self,amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance
    
    
Mahi = Bank('Mahi','Savings')
# print(Mahi.__balance) Can't access private attributes
print(Mahi._account_holdar) #Protected attributes can access
print(Mahi.account_type) #Public attributes can access

Mahi.deposit(5000)
print(Mahi.get_balance())

print(Mahi._Bank__balance) #We can access private attributes using this


