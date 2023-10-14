#The Alchemists who make Potions
from Potions import Potion, Erumpent_Potion , Felix_Felicis, Polyjuice_Potion


class Alchemist:
    def __init__(self,name,known_potions=[], stock=[], gold = 500):
        self.name= name
        self.known_potions = known_potions 
        self.stock = stock
        self.gold = gold

    def invent_potion(self,name="", effect=""):
        print(f"{self.name} is devising a completely new potion")
        if len(name) == 0:
            name = input("New potion's name: ")
        if len(effect) == 0 :
            effect = input("New potion's effect: ")

        invention = Potion(name,effect, self.name)
        
        self.known_potions.append(invention)
        return self

    def info(self):
        index = 1
        print(f" {self.name}\n____________ \n Known Potions \n _______________\n")
        for each in self.known_potions:
            print(each)
        print(f"\n________________\n Stock \n ________________________")
        for each in self.stock:
            print(f"({index}) {each}")
            index += 1
        return self

        
    
    def __str__(self):
        return f"{self.name}"
    
    def learn(self):
        print("Learning a Potion from the stock")
        indice=1
        for item in self.stock:
            print(f"({indice}) {item.name}")
            indice+=1
        seleccion=input("option:")

        self.known_potions.append(self.stock[int(seleccion)-1])
        self.stock.pop(int(seleccion)-1)
        return self

    def brew(self):
        indice =1
        if len(self.stock) < 10:
            
            print("Which Potion would you like to brew")
            for item in self.known_potions:
                print(f"({indice}) {item.name}")
                
            seleccion = input("Which Potion?")
            self.stock.append(self.known_potions[int(seleccion)-1])
            print(f"You have succesfully brewed a {self.known_potions[int(seleccion)-1]}")
            
        else:
            print(f" There's not enough Space in {self.name}'s Stock to brew a Potion")
        
        return self


        

#Alchemists
Archimedes = Alchemist("Archimedes", [Erumpent_Potion, Felix_Felicis], [Polyjuice_Potion,Erumpent_Potion])
Paracelsus = Alchemist("Paracelsus")

#Executing Methods


Paracelsus.info()




