from ast import Import
from random import random


class Ability:
    def __inti__(self, name = "brandon", max_damage = 100):
        self.name = name
        self.max_damage = max_damage


    def attack(self):
        attack_value = random.range(0, self.max_damage)
        print(attack_value)

        return attack_value

ability = Ability("super fast", 100)
ability.attack()
