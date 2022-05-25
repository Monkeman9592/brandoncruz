import random

class Armors:
    def __init__(self , name , armor_strength ):
        self.name = name
        self.armor_strength = armor_strength

    def __repr__(self): 
       return f'Armors({self.name}, {self.armor_strength})'

    def defend(self):
        defend_value = random.randrange(0, self.armor_strength)


        return defend_value

Armor1 = Armors("strong defence", 100)

print(Armor1.defend())