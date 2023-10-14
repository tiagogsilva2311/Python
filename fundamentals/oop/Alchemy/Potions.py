class Potion:
    def __init__(self, name, effect, creator):
        self.name =name
        self.effect = effect
        self.creator = creator
        
    def info(self):
        print(f"{self.name}: \n {self.effect},  \n  Created by: {self.creator}")

    #Metodo Str le da una Label al texto para ahcer n print del texto en vez de la dirección de memoria
    def __str__(self):
        return f"{self.name}"
    
    


#Potions
Erumpent_Potion = Potion("Erumpent Potion","A Very Explosive Potion", "JK Rowling")

Felix_Felicis= Potion("Felix Felicis","Drink this to have the perfect day","A Random Wizard")

Polyjuice_Potion = Potion("Polyjuice Potion","Transforms you into a target that you have genetic material for","Ugandan Knuckles")

#Executing Methods
Erumpent_Potion.info()
Felix_Felicis.info()
Polyjuice_Potion.info()