from hero import *
import unittest

class TestHero(unittest.TestCase):

    def test_init(self):
        #first check if hero.name is a string
        self.assertEqual(type(Hero(100, "1000").name), type(""))