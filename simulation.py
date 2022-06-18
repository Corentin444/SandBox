import pygame

from materials.air import Air
from materials.dirt import Dirt
from materials.grass import Grass
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
        self.current_world = [[Air() for _ in range(self.cols)] for _ in range(self.rows)]
        self.setting = setting

    def reset_world(self):
        self.current_world = [[Air() for _ in range(self.cols)] for _ in range(self.rows)]

    def update_world(self):
        for x in range(self.rows - 1):
            for y in range(self.cols - 1):
                cell = self.current_world[x][y]
                if not cell.done:
                    if cell.material == "sand":
                        self.update_sand(x, y, cell)
                    elif cell.material == "water":
                        self.update_water(x, y, cell)
                    elif cell.state == "solid":
                        self.update_solid(x, y, cell)
                    cell.done = True

        # set all cell to not done
        for x in range(self.rows - 1):
            for y in range(self.cols - 1):
                self.current_world[x][y].done = False

    def update_sand(self, x, y, sand):
        # check if the cell bellow is available
        if self.can_move_to(x, y, x, y + 1):
            self.move_to(x, y, x, y + 1)

        # check if the bottom right is available
        elif self.can_move_to(x, y, x + sand.way, y + 1):
            self.move_to(x, y, x + sand.way, y + 1)

        # check if the bottom left is available
        elif self.can_move_to(x, y, x - sand.way, y + 1):
            self.move_to(x, y, x - sand.way, y + 1)

        # check if the cell bellow is water
        elif self.current_world[x][y + 1].material == "water":
            self.move_to(x, y, x, y + 1)

    def update_water(self, x, y, water):
        if self.can_move_to(x, y, x, y + 1):
            self.move_to(x, y, x, y + 1)

        elif self.can_move_to(x, y, x - water.way, y + 1):
            self.move_to(x, y, x - water.way, y + 1)

        elif self.can_move_to(x, y, x + water.way, y + 1):
            self.move_to(x, y, x + water.way, y + 1)

        elif self.can_move_to(x, y, x - water.way, y):
            self.move_to(x, y, x - water.way, y)

        elif self.can_move_to(x, y, x + water.way, y):
            self.move_to(x, y, x + water.way, y)

    def instantiate(self, x, y, value):
        # check the value and set the cell new material
        if value == self.setting.materials.index("Empty"):
            self.current_world[x][y] = Air()
        elif value == self.setting.materials.index("Sand"):
            self.current_world[x][y] = Sand()
        elif value == self.setting.materials.index("Water"):
            self.current_world[x][y] = Water()
        elif value == self.setting.materials.index("Stone"):
            self.current_world[x][y] = Stone()
        elif value == self.setting.materials.index("Dirt"):
            self.current_world[x][y] = Dirt()
        elif value == self.setting.materials.index("Grass"):
            self.current_world[x][y] = Grass()

    def update_solid(self, x, y, cell):
        if self.can_move_to(x, y, x, y + 1):
            self.move_to(x, y, x, y + 1)

    def move_to(self, x, y, target_x, target_y):
        tmp = self.current_world[x][y]
        self.current_world[x][y] = self.current_world[target_x][target_y]
        self.current_world[target_x][target_y] = tmp
        self.current_world[x][y].done = True

    def can_move_to(self, x, y, target_x, target_y):
        if self.current_world[target_x][target_y].material == "air":
            return True

    def draw(self):
        for x in range(self.rows):
            for y in range(self.cols):
                pygame.draw.rect(self.screen, self.current_world[x][y].color,
                                 [int(x * self.cell_size), int((y - 1) * self.cell_size),
                                  self.cell_size - self.setting.offset,
                                  self.cell_size - self.setting.offset
                                  ])
