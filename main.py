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
    max_width = 800
    max_height = 600
    size = (min(r.width, max_width), min(r.height, max_height))
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()

    # Save a PNG
    r.export('./test.png')

    shift = False
    scroll_x = 0
    scroll_y = 0
    scroll_speed = 15

    # Show graph
    while True:
        screen.fill((255, 255, 255))
        screen.blit(r.surface, (-scroll_x, -scroll_y))
        pygame.display.flip()

        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

            # Shift key
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                    shift = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                    shift = False

            # Scrolling input
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4 and not shift:  # Up
                    scroll_y -= scroll_speed
                if event.button == 5 and not shift:  # Down
                    scroll_y += scroll_speed
                if event.button == 4 and shift:  # Left
                    scroll_x -= scroll_speed
                if event.button == 5 and shift:  # Right
                    scroll_x += scroll_speed

            # Scrolling constraint
            scroll_x = min(max(scroll_x, 0), r.width - size[0])
            scroll_y = min(max(scroll_y, 0), r.height - size[1])


if __name__ == '__main__':
    main()
