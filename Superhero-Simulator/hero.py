import random
from unicodedata import name
from ability import Ability
from armor import Armors

class Hero:


  def __init__(self, name = "Hero", starting_health=1000):
    
    self.name = name

    self.starting_health = starting_health

    self.current_health = starting_health 

    self.armor = []
    self.ability = []
  
  def add_ability(self, ability):
    self.ability.append(ability)
    return self.ability

  def attack(self):
    attack_value = 0
    for ability in self.ability:
      attack_value += ability.attack()
    return attack_value

  def add_armor(self,armor):
    self.armor.append(armor)
    return self.armor

  def defend(self):
    defend_value = 0 
    for armor in self.armor:
      defend_value += armor.defend()
    return defend_value





  
  def battle(self, opponent):
    ''' Current Hero will take turns battling the opponent hero passed in.
    '''
    heroes_names = []

    heroes_names.append(self.name)
    heroes_names.append(opponent.name)

    winner = random.choice (heroes_names)
    loser = []

    for hero in heroes_names:
      if hero != winner:
        loser.append (name)


    print(f'{winner} has defeated {loser}')

    return winner 


if __name__ == "__main__":
   
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")

    hero1.battle(hero2)

    

    ability1 = Ability ("super fast", 100)
    ability2 = Ability ("bark",100)
    ability3 = Ability ("punch", 100)  

    hero1.add_ability(ability2)
    hero2.add_ability(ability3)

    print(hero1.attack())

    armor1 = Armors ("rusty spoons", 100)
    hero1.add_armor(armor1)

    print(hero1.defend())


