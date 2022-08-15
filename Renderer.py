from Graph import Graph

import pygame


class Renderer:

    def __init__(self, width: int, height: int, line_thickness: int, node_thickness: int):
        pygame.init()
        self.width = width
        self.height = height
        self.line_thickness = line_thickness
        self.node_thickness = node_thickness
        self.surface = pygame.Surface((width, height))
        self.surface.fill((255, 255, 255))

    def render(self, graph: Graph) -> None:
        """Draws a graph to the renderer's surface object.
        Call this function once, then blit it to the window surface every frame."""

        # Draw connections
        for node1 in graph.nodes:
            point1 = (node1.position_x, node1.position_y)
            for node2 in node1.dependants:
                point2 = (node2.position_x, node2.position_y)

                # TODO: Clean up connection drawing code
                line_color = (0, 0, 0)
                pygame.draw.line(self.surface, line_color, point1, point2, self.line_thickness)

        # Draw nodes
        for node in graph.nodes:
            node.draw(self.surface, self.node_thickness)
