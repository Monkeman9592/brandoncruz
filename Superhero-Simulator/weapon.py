improt random

class Weapon(Ability):
  def attack(self):
    attack_value = random.randrange(0, self.max_damage)
    attack_value / self.max_damage()
    
    return attack
    
    
   
    
    """  This method returns a random value
    between one half to the full attack power of the weapon.
    """
    # TODO: Use integer division to find half of the max_damage value
    # then return a random integer between half of max_damage and max_damage

