import random

from ability import Ability

class Weapon(Ability):

  def attack(self):
    attack_value = random.randrange(int(self.max_damage / 2), self.max_damage)

    
    return attack_value
    
    
   
    
    """  This method returns a random value
    between one half to the full attack power of the weapon.
    """
    # TODO: Use integer division to find half of the max_damage value
    # then return a random integer between half of max_damage and max_damage

Weapon1 = Weapon("spoons", 50)

print(Weapon1.attack())