from random import randrange


class Water:
    def __init__(self):
        self.material = "water"
        self.state = "liquid"
        self.weight = 997
        self.fire_level = 0
        self.done = False
        self.color = 0, 0, 200
        self.way = randrange(2) * 2 - 1
