import pygame
from math import floor
from simulation import Simulation
from settings import Setting

setting = Setting()

screen = pygame.display.set_mode(setting.size)
setting.window = screen
clock = pygame.time.Clock()

simulation = Simulation(setting)

updateRate = 0.05
countDownMS = updateRate
toggleCounterMS = 0.0
toggleThresholdMS = 0.125
isPaused = False
run = True
material = 1
while run:
    clock.tick(setting.fps)
    pygame.display.set_caption("Falling Sand - FPS: {}".format(int(clock.get_fps())))
    # handle event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_SPACE:
                isPaused = not isPaused
            if event.key == pygame.K_r:
                simulation.reset_world()
            if event.key == pygame.K_t:
                if material < 3:
                    material += 1
                else:
                    material = 0

    if not isPaused:
        simulation.update_world()
        countDownMS = updateRate
        simulation.draw()

    sec = clock.get_rawtime() / 100
    countDownMS -= sec
    toggleCounterMS += sec

    if countDownMS < 0.0:

        if pygame.mouse.get_pressed()[0]:
            mx, my = pygame.mouse.get_pos()
            _x = floor(mx / setting.cell_size)
            _y = floor(my / setting.cell_size) + 1
            simulation.instantiate(_x, _y, material)

    pygame.display.flip()

pygame.quit()
