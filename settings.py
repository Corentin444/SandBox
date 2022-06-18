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

    materials = ["Empty", "Sand", "Water", "Stone", "Dirt", "Grass"]
