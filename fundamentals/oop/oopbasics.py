class Pizza:
    def __init__(self, masa, forma, toppings,tamaño):
        self.mass = masa
        self.shape = forma
        self.toppings = toppings
        self.size = tamaño
        self.temperature = 0
        self.slices = 6
#arriba la clase abajo el metodo que aumenta la temperatura
    def raisetemp(self): #metodo que aumenta temp en 30 degs
            if self.temperature <=100:
                print("Calentando la Pizza")
                self.temperature += 30
            else:
                print ("Se quma la pizza!!"),

        
    def comer (self): #sacar pedazos de pizza
            if self.slices>0:
                self.slices -= 1
            else:
                print("No hay mas Pizza")

#Objeto
pizza1 = Pizza("tradicional", "cuadrada",["tocineta", "champiñones"],"personal")

print("pedazos:", pizza1.slices)

pizza1.comer()

print ("quedan", pizza1.slices, "pedazos")