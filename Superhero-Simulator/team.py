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

    def living_member(self):
        if self.deaths() == 0:
            print(f"{self} is ready to fight")
        elif self.deaths <= 1: 
            print(f"{self} can no longer compeat")

        

    def team_attack(self, another_team):
        ''' if self.heroes gives me access to heroes on self's team 
            then another_team.heroes gives me acces to heroes on another_team's team
        '''
        another_team = random.choice(another_team.heroes)
        print(f"{another_team}")
        self = random.choice(self.heroes)
        print(F"{self}")
        self.living_member()
        
            
    def revive (self):
        self.current_health = 100
        self.death = 0




Team1 = Team("Blanh")
Team2 = Team("baka")





#Team1.view_all_heroes()  
# Team1.team_attack(Team2)