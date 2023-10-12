class Bank:
    def __init__(self,balance):
        self.Balance = balance
        self.MaxWithdraw = 50000
        self.MinWithdraw = 500

    def BalanceCheck(self):
        print(self.Balance)
    
    def Deposite(self,amount):
        self.Balance += amount

    def WithDraw(self,amount):
        if amount<self.MinWithdraw or amount>self.MaxWithdraw:
            print("You can't withdraw below 500 and upper 50000")
        else:
            self.Balance -= amount
            print("Here's Your Money: ",amount)
            print("Your New Balance Is: ",self.Balance)
            

DBBL = Bank(100000)
DBBL.WithDraw(400)
DBBL.BalanceCheck()
DBBL.Deposite(50000)
DBBL.BalanceCheck()
DBBL.WithDraw(20000)
DBBL.BalanceCheck()