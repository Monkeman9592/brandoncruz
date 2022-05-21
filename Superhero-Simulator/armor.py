import random

class Armors:
    def __init__(self , name , armor_strength ):
        self.name = name
        self.armer_strength = armor_strength

    def __repr__(self): 
       return f'Armors({self.name}, {self.armer_strength})'

    def defend(self):
        defend_value = random.randrange(0, self.armer_strength)
        print(defend_value)

        return defend_value

Armor1 = Armors("strong defence", 100)

print(Armor1.defend)