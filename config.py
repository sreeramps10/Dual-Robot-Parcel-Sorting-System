# === Grid Settings ===
GRID_WIDTH = 20
GRID_HEIGHT = 20
CELL_SIZE = 40

# === Simulation Timing ===
FPS = 30
PARCEL_INTERVAL = 20
DELIVERY_THRESHOLD = 20

# === Robot Settings ===
ROBOT_SPEED = 0.2
ROBOT_HOME = [(0, 0), (0, 2)]

# === Colours ===
BG_COLOUR = (255, 255, 255)
GRID_COLOUR = (200, 200, 200)
ROBOT_COLOUR = (0, 0, 255)
PARCEL_COLOUR = (255, 0, 0)
PICKUP_COLOUR = (0, 255, 0)
DELIVERY_COLOUR = (255, 255, 0)
OBSTACLE_COLOUR = (0, 0, 0)


# === Obstacle Settings ===
OBSTACLE_LIST = [
    (5, 5), (6, 5), (7, 5), (8, 5), (9, 5),
    (10, 5), (11, 5), (12, 5), (13, 5), (14, 5),
    (5, 6), (5, 7), (5, 8), (5, 9),
    (15, 15), (16, 15), (17, 15), (15, 16), (15, 17),
    (10, 10), (11, 10), (12, 10),
    (3, 14), (4, 14), (5, 14),
    (8, 12), (9, 12), (10, 12),
    (12, 3), (13, 3), (14, 3),
    (1, 1), (1, 2), (1, 3),
    (19, 19), (19, 18), (18, 19),
]


# === Others ===
MAX_PARCELS = 5



