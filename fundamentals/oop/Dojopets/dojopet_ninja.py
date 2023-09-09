from dojopet_mascot import mascot, doggy, kitty

class ninja:
    def __init__(self,name,pets,prize,food):
        self.name = name
        self.pets = pets
        self.prize = prize
        self.food= food

    def walk(self):
        print("Walking The Pets \n ____________________")
        for each in self.pets:
            each.play()
        return self

    def feed(self,):
        
        print("Feeding the pets \n __________________")
        for each in self.pets:
            
            print(f" Yummy, {self.name} is Feeding {each.treat} to {each.name}") 
            each.eat()
            
        return self


    def bathe(self):
        print ("Bathing the Pets \n _____________________")
        for each in self.pets:
            print(f"{self.name} is Bathing {each.name}")
            each.sound()
        return self







