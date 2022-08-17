from core.Graph import Graph
from positioners.TieredPositioner import TieredPositioner
from core.Renderer import Renderer

import pygame
import sys


def main():
    pygame.init()

    # Select font
    font = pygame.font.SysFont('freesansbold.ttf', 24)

    # Import graph from JSON file
    g = Graph('./projects.json', font)

    # Set node positions
    rp = TieredPositioner(offset=(16, 16), spacing=(16, 48))
    width, height = rp.place_graph(g)

    # Render graph
    r = Renderer(width, height, 1, 1, font)
    r.render(g)

    # Create window
    size = (r.width, r.height)
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()

    # Save a PNG
    r.export('./test.png')

    # Show graph
    while True:
        screen.fill((255, 255, 255))
        screen.blit(r.surface, (0, 0))
        pygame.display.flip()

        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)


if __name__ == '__main__':
    main()
