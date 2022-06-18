from random import randrange


class Air:
    def __init__(self):
        self.material = "air"
        self.state = "empty"
        self.weight = 1
        self.fire_level = 0
        self.done = False
        self.color = 0, 0, 0
        self.way = randrange(2) - 1
