import pygame
import sys
import config
from simulation import Simulation
from grid import draw_grid, draw_obstacles

def main():
    pygame.init()
    screen = pygame.display.set_mode(
        (config.GRID_WIDTH * config.CELL_SIZE, config.GRID_HEIGHT * config.CELL_SIZE)
    )
    pygame.display.set_caption("Multi-Robot Parcel Sorting Simulation")

    clock = pygame.time.Clock()
    simulation = Simulation()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(config.BG_COLOUR)

        draw_grid(screen)
        draw_obstacles(screen)

        simulation.update()
        simulation.draw(screen)

        pygame.display.flip()

        clock.tick(config.FPS)


    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
