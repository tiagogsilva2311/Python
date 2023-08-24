#apoyate de las ayudantias desde el 20 Santi, tu puedes!!!!!

#CLASE CUENTA BANCARIA

class Account:
    #Los Atributos de clase se definen fuera de cualquier metodo de isntancia (el init) y se comparten entre todas las instancias

    bank_name = "Holobank"
    
    def __init__(self, user, balance =0,interest_rate= 0):
        self.balance = balance
        self.user= user
        self.interest= interest_rate


class Holder:
    def __init__(self,first_name,last_name, email, accounts, balance= 0):
        self.first_name = first_name
        self.last_name = last_name
        self.email= email
        self.account = accounts
        self.balance = balance

    def userinfo(self):

        print(f" User Information \n User: {self.first_name} {self.last_name}  \n Email: {self.email} " )

    def withdraw(self,amount):
        if self.balance>0 and self.balance>amount:
            self.balance -= amount
            print(f" {self.first_name} withdrew ${amount} from their account, remaining balance is ${self.balance}")
            
        else:
            print(f"Insufficient funds, remaining balance is {self.balance}")

    def deposit(self, amount):
        self.balance += (amount)
        print(f" {self.first_name} deposited ${amount} to their account, remaining balance is ${self.balance}")
        return self

    def transfer(self,amount,other_user):
        if self.balance >= amount:
            self.balance -=amount
            other_user.balance +=amount
            print(f"{self.first_name} has succesfully transferred ${amount} to {other_user.first_name}, \n remaining balance: ${self.balance}")
        else: 
            print(f"{self.first_name} has insufficient funds on their bank account \n Remaining Balance: ${self.balance}")
        return self

    def compare(self, user2):
        print(f"{self.first_name} has a balance of ${self.balance} , and {user2.first_name} has a balance of ${user2.balance} ", )
        return self
    





Fauna = Holder("Fauna","Ceres","mama_nature42@araara.org","yes")
Bae = Holder("Baelz", "Hakos","hakotaro@chaosmail.au","many accounts",0)
Kiara = Holder("Kiara","Takanashi","takanashikiwawa@phoenixmail.at","yes")

Fauna.transfer(100,Bae)

