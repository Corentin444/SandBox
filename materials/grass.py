from random import randrange


class Grass:
    def __init__(self):
        self.material = "grass"
        self.state = "solid"
        self.weight = 600
        self.fire_level = 0
        self.done = False
        self.color = 30, 90, 0
        self.way = randrange(2) * 2 - 1
