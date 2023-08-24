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
        print("zzzz")
        self.energy += 25

    def eat(self,weight):
        print("Yummy!")
        self.energy += 5
        self.health +=10
        print(self.treat + ", " + str(weight) + " kgs")

    def play(self):
        print("Playing!")
        self.health += 5

    def sound(self):
        print("pet noise")

class doggy(mascot):
    def __init__(self, name, treat, health, energy):
        super().__init__(name, "dog", treat, health, energy)

    def sound(self):
        print("Bark!, Bark!")

class kitty(mascot):
    def __init__(self, name, treat, health, energy):
        super().__init__(name, "cat", treat, health, energy)

    def sound(self):
        print("meeeow!!")

class ninja:
    def __init__(self,name,ln,pets,prize,food):
        self.name = name
        self.ln = ln
        self.pets = pets
        self.prize = prize
        self.food= food

    def walk(self):
        print("Walking")
        for each in self.pets:
            each.play()

    def feed(self, weight):
        print("yuuum")
        for each in self.pets:
            each.eat(weight)

    def bathe(self):
        for each in self.pets:
            each.sound()




firulais = doggy("firulais","chow",50,25)

tostadora = kitty("Tostaddora","churus",90,10)

carlos = ninja("Carlos","perez",[firulais, tostadora],"meat",{"dog":"purina", "cat":"cat chow"})

carlos.feed(50)

print(tostadora.type)