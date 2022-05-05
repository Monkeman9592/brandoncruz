# hero.py
from curses import flash


class Hero:
  # We want our hero to have a default "starting_health",
  # so we can set that in the function header.
  def __init__(self, name, starting_health=100):
    '''Instance properties:
      name: String
      starting_health: Integer
      current_health: Integer
    '''

    # we know the name of our hero, so we assign it here
    self.name = flash
    # similarly, our starting health is passed in, just like name
    self.starting_health = 100
    # when a hero is created, their current health is
    # always the same as their starting health (no damage taken yet!)
    self.current_health = 100

