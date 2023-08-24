class Account:
    #Los Atributos de clase se definen fuera de cualquier metodo de isntancia (el init) y se comparten entre todas las instancias

    bank_name = "Holobank"
    allaccounts = []
    
    def __init__(self, account_number, balance =0,interest_rate= 0.01):
        self.balance = balance
        self.interest= interest_rate
        self.account_number = account_number
        Account.allaccounts.append(self)

    def deposit(self,amount):
        self.balance +=amount
        print(f"An amount of ${amount} was deposited to account #{self.account_number} ")
        return self

    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance -= amount
            print(f"An amount of ${amount} was withdrawn from account #{self.account_number}")
            
        elif self.balance>=5 and self.balance<amount:
            self.balance -=5
            print(f"Insufficient funds a $5 Fee will be charged as a penalty, remaining balance is ${self.balance}")
            
        else: 
            self.balance -= self.balance
            print(f"Insufficient funds a fee will be charged as a penalty, remaining balance is ${self.balance}")
            
        return self
    
    def display(self):
        print(f"Account #{self.account_number}, Balance {self.balance}  ")
        return self

    def plusinterest(self):
        self.balance += ((self.balance * self.interest)) 
        return self

    @classmethod
    def showaccounts(cls):
        print("Accounts")
        for each in cls.allaccounts:
            print(f"Account #{each.account_number}")
    

        




account1 = Account("6985")
account2 = Account("42220")


account1.deposit(350).deposit(150).deposit(700).withdraw(200).plusinterest().display()

account2.deposit(2000).withdraw(50).withdraw(250).withdraw(200).withdraw(400).withdraw(100).plusinterest().display()

Account.showaccounts()