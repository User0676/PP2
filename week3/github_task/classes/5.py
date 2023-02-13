class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self,money):
        self.balance = self.balance + money


    def windraw(self,amount):
        if amount>self.balance:
            print("You don't have enought money")
        else:
            self.balance = self.balance - amount
    def currentBalance(self):
        print(self.balance)

owner1=Account("Ali",20000)
owner1.currentBalance()
owner1.deposit(2000)
owner1.currentBalance()
owner1.windraw(5000)
owner1.currentBalance()
owner1.windraw(1000000)


