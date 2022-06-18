from random import randrange


class Dirt:
    def __init__(self):
        self.material = "dirt"
        self.state = "solid"
        self.weight = 1700
        self.fire_level = 0
        self.done = False
        self.color = 90, 30, 0
        self.way = randrange(2) * 2 - 1
