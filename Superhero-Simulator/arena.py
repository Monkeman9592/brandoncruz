from ast import Return
from ability import Ability
from weapon import Weapon
from armor import Armors
from hero import Hero
from team import Team

class Arena:
  def __init__(self):
    '''Instantiate properties
        team_one: None
        team_two: None
    '''
    self.team_one = []
    self.team_two = []
    
    
    
    
    # TODO: create instance variables named team_one and team_two that
    # will hold our teams.

  def create_ability(self):
    '''Prompt for Ability information.
      return Ability with values from user Input
    '''
    name = input("What is the ability name?  ")
    max_damage = input("What is the max damage of the ability?  ")

    return Ability(name, max_damage)

  def create_weapon(self):
    
    weapon = input("what weapon would you like to make")
    max_damage = input("how much damage would you like to set to this weapon")
    
    return (weapon,max_damage)
  
    '''Prompt user for Weapon information
        return Weapon with values from user input.
    '''
    # TODO: This method will allow a user to create a weapon.
    # Prompt the user for the necessary information to create a new weapon object.
    # return the new weapon object.
    pass

  def create_armor(self):
    
    armor = input("what kind of armor would you like to give you hero")
    armor_strength = input("how much strength would you like to set this armor to")
    
    return (armor, armor_strength)
    '''Prompt user for Armor information
      return Armor with values from user input.
    '''
    # TODO:This method will allow a user to create a piece of armor.
    #  Prompt the user for the necessary information to create a new armor object.
    #  return the new armor object with values set by user.
      # pass

  def create_hero(self):
    '''Prompt user for Hero information
      return Hero with values from user input.
    '''
    ''' if self.create_ability gives me access to create_ability methods of self 
        then hero.add_ability gives me access to add_abilty method  of hero
    '''
    hero_name = input("Hero's name: ")
    hero = Hero(hero_name)
    add_item = None
    while add_item != "4":
            
      add_item = input("[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice: ")
            
      if add_item == "1":

        new_ability = self.create_ability()
        hero.add_ability(new_ability) 
       
        # TODO add an ability to the hero
        # HINT: First create the ability, then add it to the hero
      elif add_item == "2":
        new_weapon = self.create_weapon()
        hero.add_weapon(new_weapon)

        # TODO add a weapon to the hero
        # HINT: First create the weapon, then add it to the hero
      elif add_item == "3":
        new_armor = self.create_armor()
        hero.add_armor(new_armor)

        # TODO add an armor to the hero
        # HINT: First create the armor, then add it to the hero
    return hero


  # build_team_one is provided to you
  def build_team_one(self):
    numOfTeamMembers = int(input("How many members would you like on Team One?\n"))
    for i in range(numOfTeamMembers):
      if i > 1:
        return True
      elif i < 5:
        return False 
      hero = self.create_hero()
      self.team_one.add_hero(hero)

    '''Prompt the user to build team_one '''
    
    # This method should allow a user to create team one.
    # Prompt the user for the number of Heroes on team one
    # call self.create_hero() for every hero that the user wants to add to team one.

    # Add the created hero to team one.
    

  # Now implement build_team_two
  #HINT: If you get stuck, look at how build_team_one is implemented
  def build_team_two(self): 
    numOfTeamMembers = int(input("How many members would you like on Team one?\n "))
    for i in range(numOfTeamMembers):
      if i > 1:
        return True
      elif i < 5:
        return False 
      hero = self.create_hero()
      self.team_two.add_hero(hero)
    '''Prompt the user to build team_two'''
    # TODO: This method should allow a user to create team two.
    # This method should allow a user to create team two.
    # Prompt the user for the number of Heroes on team two
    # call self.create_hero() for every hero that the user wants to add to team two.
    # Add the created hero to team two.
    pass

  def team_battle(self):
      

    '''Battle team_one and team_two together.'''
    # TODO: This method should battle the teams together.
    # Call the attack method that exists in your team objects
    # for that battle functionality.
    pass

  def show_stats(self):
    '''Prints team statistics to terminal.'''
    # TODO: This method should print out battle statistics
    # including each team's average kill/death ratio.
    # Required Stats:
    #     Show surviving heroes.
    #     Declare winning team
    #     Show both teams average kill/death ratio.
    # Some help on how to achieve these tasks:
    # TODO: for each team, loop through all of their heroes,
    # and use the is_alive() method to check for alive heroes,
    # printing their names and increasing the count if they're alive.
    #
    # TODO: based off of your count of alive heroes,
    # you can see which team has more alive heroes, and therefore,
    # declare which team is the winning team
    #
    # TODO for each team, calculate the total kills and deaths for each hero,
    # find the average kills and deaths by dividing the totals by the number of heroes.
    # finally, divide the average number of kills by the average number of deaths for each team

    print("\n")
    print(self.team_one.name + " statistics: ")
    self.team_one.stats()
    print("\n")
    print(self.team_two.name + " statistics: ")
    self.team_two.stats()
    print("\n")

    # This is how to calculate the average K/D for Team One
    team_kills = 0
    team_deaths = 0
    for hero in self.team_one.heroes:
        team_kills += hero.kills
        team_deaths += hero.deaths
    if team_deaths == 0:
        team_deaths = 1
    print(self.team_one.name + " average K/D was: " + str(team_kills/team_deaths))

    # TODO: Now display the average K/D for Team Two

    # Here is a way to list the heroes from Team One that survived
    for hero in self.team_one.heroes:
        if hero.deaths == 0:
            print("survived from " + self.team_one.name + ": " + hero.name)

    #TODO: Now list the heroes from Team Two that survived

    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()

