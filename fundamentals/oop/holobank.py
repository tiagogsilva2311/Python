#Clase Cuenta bancaria
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
    
    

    def plusinterest(self):
        self.balance += ((self.balance * self.interest)) 
        return self

    @classmethod
    def showaccounts(cls):
        print("Accounts")
        for each in cls.allaccounts:
            print(f"Account #{each.account_number}")
    

        






#Clase Usuario

class Holder:
    def __init__(self,first_name,last_name, email,account_number):
        self.first_name = first_name
        self.last_name = last_name
        self.email= email
        self.account = Account(account_number =account_number, interest_rate=0.02, balance= 0)
        

    def userinfo(self):

        print(f" User Information \n User: {self.first_name} {self.last_name}  \n Email: {self.email} " )

    def withdraw(self,amount):
        if self.account.balance>0 and self.account.balance>amount:
            self.account.balance -= amount
            print(f" {self.first_name} withdrew ${amount} from their account, remaining balance is ${self.account.balance}")
            
        else:
            print(f"Insufficient funds, remaining balance is {self.balance}")

            return self

    def deposit(self, amount):
        self.account.balance += (amount)
        print(f" {self.first_name} deposited ${amount} to their account, remaining balance is ${self.account.balance}")
        return self

    def transfer(self,amount,other_user):
        if self.account.balance >= amount:
            self.account.balance -=amount
            other_user.account.balance +=amount
            print(f"{self.first_name} has succesfully transferred ${amount} to {other_user.first_name}, \n remaining balance: ${self.account.balance}")
        else: 
            print(f"{self.first_name} has insufficient funds on their bank account \n Remaining Balance: ${self.account.balance}")
        return self

    def compare(self, user2):
        print(f"{self.first_name} has a balance of ${self.account.balance} , and {user2.first_name} has a balance of ${user2.account.balance} ", )
        return self
    
    
    def display(self):
        print(f"Account #{self.account.account_number} \n  ------------------------\n Holder: {self.first_name} {self.last_name} \n  Balance: {self.account.balance}  ")
        return self.account


Fauna = Holder("Fauna","Ceres","mama_nature42@araara.org", "42694234")
Bae = Holder("Baelz", "Hakos","hakotaro@chaosmail.au", "41405")
Kiara = Holder("Kiara","Takanashi","takanashikiwawa@phoenixmail.at", "654321")



#first user 3 deposits 1 transfer
Fauna.deposit(1200).deposit(600).deposit(3000).transfer(500,Bae).compare(Bae)

#second user 2 deposits 2 transfer
Bae.deposit(600).deposit(200).transfer(150,Fauna).transfer(350,Kiara).compare(Kiara).compare(Fauna)

#third user 1 deposit 3 transfers
Kiara.deposit(750).transfer(250, Fauna).transfer(20, Bae).transfer(150, Fauna)

Fauna.account.plusinterest()
Fauna.display()




