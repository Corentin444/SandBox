import numpy as np
import pygame
import random

from materials.air import Air
from materials.sand import Sand
from materials.stone import Stone
from materials.water import Water


class Simulation:
    def __init__(self, setting):
        self.rows = setting.rows + 1
        self.cols = setting.cols + 1
        self.cell_size = setting.cell_size
        self.screen = setting.window

        # initialize world
        self.reset_world()
        self.setting = setting

    def reset_world(self):
        self.previous_world = [[Air() for _ in range(self.cols)] for _ in range(self.rows)]
        self.current_world = [[Air() for _ in range(self.cols)] for _ in range(self.rows)]

    def update_world(self):
        for x in range(self.rows - 1):
            for y in range(self.cols - 1):
                cell = self.previous_world[x][y]
                if not cell.done:
                    if cell.material == "sand":
                        self.update_sand(x, y, cell)
                    elif cell.material == "water":
                        self.update_water(x, y, cell)
                    elif cell.material == "stone":
                        self.update_stone(x, y, cell)
                    cell.done = True

        # set all cell to not done
        for x in range(self.rows - 1):
            for y in range(self.cols - 1):
                self.previous_world[x][y].done = False

    def update_sand(self, x, y, sand):
        # check if the cell bellow is available
        if self.previous_world[x][y + 1].material == "air":
            self.current_world[x][y] = Air()
            self.current_world[x][y + 1] = sand

        # check if the bottom left and bottom right cells are available
        elif self.previous_world[x - 1][y + 1].material == "air" and self.previous_world[x + 1][
            y + 1].material == "air":
            # pick a random cell between the two
            self.current_world[x][y] = Air()

            if random.randint(0, 1) == 0:
                self.current_world[x - 1][y + 1] = sand
            else:
                self.current_world[x + 1][y + 1] = sand

        # check if the bottom right is available
        elif self.previous_world[x + 1][y + 1].material == "air":
            self.current_world[x][y] = Air()
            self.current_world[x + 1][y + 1] = sand

        # check if the bottom left is available
        elif self.previous_world[x - 1][y + 1].material == "air":
            self.current_world[x][y] = Air()
            self.current_world[x - 1][y + 1] = sand

    def update_water(self, x, y, water):
        # check if the cell bellow is available
        if self.previous_world[x][y + 1].material == "air":
            self.current_world[x][y] = Air()
            self.current_world[x][y + 1] = water

        # check if the right cell is available
        elif self.previous_world[x + 1][y].material == "air":
            self.current_world[x][y] = Air()
            self.current_world[x + 1][y] = water

    def instantiate(self, x, y, value):
        # check the value and set the cell new material
        if value == self.setting.EMPTY:
            self.current_world[x][y] = Air()
        elif value == self.setting.SAND:
            self.current_world[x][y] = Sand()
        elif value == self.setting.WATER:
            self.current_world[x][y] = Water()
        elif value == self.setting.STONE:
            self.current_world[x][y] = Stone()

    def update_stone(self, x, y, stone):
        pass

    def draw(self):
        for x in range(self.rows):
            for y in range(self.cols):
                val = self.current_world[x][y]
                self.previous_world[x][y] = val
                pygame.draw.rect(self.screen, val.color, [int(x * self.cell_size), int((y - 1) * self.cell_size),
                                                          self.cell_size - self.setting.offset,
                                                          self.cell_size - self.setting.offset
                                                          ])
