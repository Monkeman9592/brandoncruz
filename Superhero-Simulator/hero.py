import random
from unicodedata import name
from ability import Ability
from armor import Armors
from weapon import Weapon


class Hero:


  def __init__(self, name = "Hero", starting_health=100):
    
    self.name = name
    self.starting_health = starting_health
    self.current_health = starting_health 
    self.armor = []
    self.ability = []
    self.weapon = []
    
    self.deaths = 0
    self.kills = 0
    
  def __repr__(self):
    return f'Hero({self.name}, {self.starting_health})'
  
  def add_ability(self, ability):
    self.ability.append(ability)
    return self.ability

  def attack(self):
    attack_value = 0
    for ability in self.ability:
      attack_value += ability.attack()
    print(f"{self.name} has {attack_value} attack")

    return attack_value

  def add_armor(self,armor):
    self.armor.append(armor)
    return self.armor

  def defend(self):
    defend_value = 0 
    for armor in self.armor:
      defend_value += armor.defend()

    print(f"{self.name} has {defend_value} defense")
    return defend_value

  def take_damage(self, incoming_damage):
    damage = incoming_damage - self.defend()
    if damage >= 0:
      self.current_health -= damage 
      
  def add_weapon(self, weapon_damage):
    self.weapon.append(weapon_damage)
    print(f"{self.name}  weapon has {self.weapon}")
    return self.weapon 
  
  
  def add_kill(self):
    self.kills += 1
    
  def add_death(self):
    self.deaths += 1


  




  def battle(self, opponent):

    if not self.ability and not opponent.ability:
      print("These heroes can't battle! They have no abilities. Average citizens they are.")
    fighting = True
    while fighting:
      #print health and start of battle 

      print(f"{self.name}: {self.current_health}")
      print(f"{opponent.name}: {opponent.current_health}")
      #attack method 
      opponent.take_damage(self.attack())
      self.take_damage(opponent.attack())

      #test 
      #print(f"{self.}")

      #if health is < 0 adds kill and death / prints winning hero
      if self.current_health <= 0:
        opponent.add_death()
        self.add_kill()
      

        print(f"{opponent.name} has defeated {self.name}")
        fighting = False


        print(f"{opponent.name} team kills: {opponent.deaths}")
        print(f"{opponent.name}had {self.kills} kill")

      elif opponent.current_health <= 0:
        self.add_death()
        opponent.add_kill()

        print(f"{self.name} has defeated {opponent.name}")
        fighting = False


        print(f"{self.name} team kills: {self.deaths}")
        print(f"{self.name} has {opponent.kills} kill ")

      


      

    
# our heros 
hero1 = Hero("Wonder Woman")
hero2 = Hero("Dumbledore")

if __name__ == "__main__":
   
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")

    

    

    ability1 = Ability ("super fast", 100)
    ability2 = Ability ("bark",100)
    ability3 = Ability ("punch", 100)  

    hero1.add_ability(ability2)
    hero2.add_ability(ability3)

    #print(hero1.attack())

    armor1 = Armors ("rusty spoons", 100)
    
    hero1.add_armor(armor1)
    hero2.add_armor(armor1)

    hero1.battle(hero2)

    Weapon1 = Weapon("spoons", 50)
    #teams
    # Team1 = Team("Blanh")
    # Team1.add_hero(hero1)
    # Team1.add_hero(hero2)
    # Team1.view_all_heroes()  

#teams


