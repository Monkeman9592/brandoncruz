import random

class Team:
    def __init__(self, name ):
        self.name = name
        self.heroes = []
        self.deaths = 0
        self.kills = 0


    def add_hero(self, hero):
        self.heroes.append(hero)
        return self.heroes


    def remove_hero(self, hero):
        self.heroes.remove(hero)
        return self.heroes

    def view_all_heroes(self):
        for item in self.heroes:
            print(F"this is our team {item.name}")

    def add_kill(self):
        self.kills += 1
    
    def add_death(self):
        self.deaths += 1


        

