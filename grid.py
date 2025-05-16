import config
import pygame

pygame.init()
screen = pygame.display.set_mode((config.GRID_WIDTH * config.CELL_SIZE, config.GRID_HEIGHT * config.CELL_SIZE))
clock = pygame.time.Clock()

def draw_grid(screen):
    for x in range(0, config.GRID_WIDTH * config.CELL_SIZE, config.CELL_SIZE):
        pygame.draw.line(screen, config.GRID_COLOUR, (x, 0), (x, config.GRID_HEIGHT * config.CELL_SIZE))
    for y in range(0, config.GRID_HEIGHT * config.CELL_SIZE, config.CELL_SIZE):
        pygame.draw.line(screen, config.GRID_COLOUR, (0, y), (config.GRID_WIDTH * config.CELL_SIZE, y))

def draw_obstacles(screen):
    for (x, y) in config.OBSTACLE_LIST:
        rect = pygame.Rect(
            x * config.CELL_SIZE,
            y * config.CELL_SIZE,
            config.CELL_SIZE,
            config.CELL_SIZE
        )
        pygame.draw.rect(screen, config.OBSTACLE_COLOUR, rect)

