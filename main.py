from core.Graph import Graph
from positioners.TieredPositioner import TieredPositioner
from core.Renderer import Renderer

import pygame
import sys


def main():
    pygame.init()

    # Import graph from JSON file
    g = Graph('./projects.json')

    # Set node positions
    rp = TieredPositioner(spacing=64)
    width, height = rp.place_graph(g)

    # Render graph
    r = Renderer(width, height, line_thickness=1, node_thickness=1)
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
