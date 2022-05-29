class Setting:
    width = 800
    height = 800
    size = (width, height)
    fps = 144
    window = None

    cell_size = 10
    cols = height // cell_size
    rows = width // cell_size
    offset = 0

    EMPTY = 0
    SAND = 1
    WATER = 2

    Colors = [(0, 0, 0), (255, 185, 30), (0, 0, 255)]
    black = (0, 0, 0)
    white = (255, 255, 255)
