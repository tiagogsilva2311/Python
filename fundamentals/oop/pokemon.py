class Pokemon:
    
    moves = []
    
    def __init__(self,species, experience_points,hp,attack,defense,special_attack, special_defense,speed,physical_evasion,special_evasion,status_evasion,moveset, hitpoints,level = 1):
        self.species= species
        
        self.hitpoints =hitpoints
        self.level= level
        self.experience_points=experience_points
        self.hp=hp
        self.attack = attack
        self.defense = defense
        self.special_attack= special_attack
        self.special_defense = special_defense
        self.speed =speed
        self.physical_evasion= physical_evasion
        self.special_evasion =special_evasion
        self.status_evasion= status_evasion
        self.moveset =moveset
        

    
        def hitpointtotal(self):
            self.hitpoints= 5 + self.level + self.hitpoints
            return self

        def statup(self, stat):
            self.stat +=1
            return self

        @classmethod
        def setmoves(cls,learn):
            self.moves.append(learn)

class Charmander(Pokemon):
    def __init__(self,nickname):
        super().__init__()
        self.nickname= nickname

