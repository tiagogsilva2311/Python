class User:
    def __init__(self,name,cuentas = None): 
        self.name = name
        self.cuentas = cuentas or []
        

    
    
    def showname(self):
        print(f"{self.name}")
        return self
    
    def addaccount(self,id):
        newaccount=Account(id)
        self.cuentas.append(newaccount)
        return self
        
    def showaccounts (self):
        print (f" \n{self.name}'s Accounts \n _________________________")
        for account in self.cuentas:
            print(account)
        print(f"\n")
            
            



class Account:

    
    def __init__(self,id, irate= 0.375 ,balance= 0):
        self.id = id
        self.balance = balance
        self.irate = irate
        
        

    def __str__(self):
        return f"Account #{self.id}, Balance: {self.balance}"

        

    def deposit(self, amount):
        self.balance += amount
        print(f" An amount of {amount} has been deposited to the Account #{self.id}" )
        return self
    
    def display(self):
        print (f" Account #{self.id}    Balance: {self.balance}")
        return self

    def growth(self, gindex = None):

        gindex = gindex or self.irate
        self.balance += self.balance*gindex
        print(f"Growing the account at an interest of {gindex}, New balance is {self.balance}")
        return self
    
    def transfer(self,target, amount):

        if (self.balance- amount) > 0 :
            self.balance -= amount
            target.balance +=amount
            print(f" an amout of {amount} has been transferred from Account #{self.id} to Account #{target.id}, \n Remaining balance: {self.balance}E")
        else:
            print(f"Account #¨{self.id} Doesn't have enough funds")
        


Elira = User("Elira")
Pomu = User("Pomu")
Feesh = User("Feesh")

Elira.addaccount("2432").addaccount("2231").cuentas[0].deposit(500).display()
Pomu.addaccount("00234")

Elira.cuentas[0].transfer(Pomu.cuentas[0],300)







