import pygame
import random


class Simulation:
    def __init__(self, setting):
        self.rows = setting.rows + 1
        self.cols = setting.cols + 1
        self.cell_size = setting.cell_size
        self.screen = setting.window
        self.colors = setting.Colors

        # initialize world
        self.previous_world = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        self.current_world = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        self.setting = setting

    def reset_world(self):
        self.previous_world = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        self.current_world = [[0 for _ in range(self.cols)] for _ in range(self.rows)]

    def update_world(self):
        for x in range(self.rows - 1):
            for y in range(self.cols - 1):
                if self.previous_world[x][y] == self.setting.SAND:
                    self.update_sand(x, y)
                if self.previous_world[x][y] == self.setting.WATER:
                    self.update_water(x, y)

    def update_sand(self, x, y):
        # check if the cell bellow is available
        if self.previous_world[x][y + 1] == self.setting.EMPTY:
            self.current_world[x][y] = self.setting.EMPTY
            self.current_world[x][y + 1] = self.setting.SAND

        # check if the bottom left and bottom right cells are available
        elif self.previous_world[x - 1][y + 1] == 0 and self.previous_world[x + 1][y + 1] == 0:
            # pick a random cell between the two
            choice = random.randint(0, 1)
            self.current_world[x][y] = 0

            if choice == 0:
                self.current_world[x - 1][y + 1] = 1
            else:
                self.current_world[x + 1][y + 1] = 1
        # check if the bottom right is available
        elif self.previous_world[x + 1][y + 1] == self.setting.EMPTY:
            self.current_world[x][y] = self.setting.EMPTY
            self.current_world[x + 1][y + 1] = self.setting.SAND
        # check if the bottom left is available
        elif self.previous_world[x - 1][y + 1] == 0:
            self.current_world[x][y] = 0
            self.current_world[x - 1][y + 1] = 1

    def update_water(self, x, y):
        # check if the cell bellow is available
        if self.previous_world[x][y + 1] == self.setting.EMPTY:
            self.current_world[x][y] = self.setting.EMPTY
            self.current_world[x][y + 1] = self.setting.WATER

    def instantiate(self, x, y, value):
        self.current_world[x][y] = value

    def draw(self):
        for x in range(self.rows):
            for y in range(self.cols):
                val = self.current_world[x][y]
                self.previous_world[x][y] = val
                pygame.draw.rect(self.screen, self.colors[val], [int(x * self.cell_size), int((y - 1) * self.cell_size),
                                                                 self.cell_size - self.setting.offset,
                                                                 self.cell_size - self.setting.offset
                                                                 ])
