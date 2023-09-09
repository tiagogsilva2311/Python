#clase Ninja atributos: nombre, apellido, mascotas, premio, comida_mascota
#metodos caminar, alimentar, bañar.

class mascot:
    def __init__(self,name,type,treat,health,energy):
        self.name = name
        self.type = type
        self.treat = treat
        self.health =health
        self.energy = energy

    def sleep(self):
        print(f" {self.name} is Sleeping, zzzz")
        self.energy += 25
        return self
    
    def eat(self):
        self.energy += 5
        self.health +=10
        
        return self

    def play(self):
        print( self.name ," is playing Excitedly!")
        self.health += 5
        return self
    
    def sound(self):
        print("pet noise")
        return self

class doggy(mascot):
    def __init__(self, name, treat, health, energy):
        super().__init__(name, "dog", treat, health, energy)
        

    def sound(self):
        print("Bark!, Bark!")
        return self

class kitty(mascot):
    def __init__(self, name, treat, health, energy):
        super().__init__(name, "cat", treat, health, energy)

    def sound(self):
        print("meeeow!!")



