from random import random

class armer_class:
    def __inti__(self , name = "brandon", armer_strength = 100):
        self.name = name
        self.armer_strength = armer_strength


    def max_block(self):
        block = random.range(0, self.armer_strength)
        print(block)

        return block

Armor = armer_class("strong defence", 100)
Armor.max_block()