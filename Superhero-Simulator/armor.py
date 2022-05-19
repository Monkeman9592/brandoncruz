from random import random

class armers:
    def __inti__(self , name = "brandon", armer_strength = 100):
        self.name = name
        self.armer_strength = armer_strength


    def max_block(self):
        block = random.range(0, self.armer_strength)
        print(block)

        return block

Armor = armers("strong defence", 100)
Armor.max_block()