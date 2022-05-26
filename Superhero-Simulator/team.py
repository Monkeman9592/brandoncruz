from hero import hero1, hero2, Hero

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

Team1 = Team("Blanh")
Team1.add_hero(hero1)
Team1.add_hero(hero2)
Team1.view_all_heroes()
        
        

