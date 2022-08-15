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

    def render(self, graph: Graph):

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
            # TODO: Clean up node drawing code (move to node class?)

            # Find bounding box
            pos_x = node.position_x - node.width / 2
            pos_y = node.position_y - node.height / 2
            bounding_box = pygame.Rect(pos_x, pos_y, node.width, node.height)

            # Draw node outline
            ring_color = (0, 0, 0)
            pygame.draw.ellipse(self.surface, (255, 255, 255), bounding_box, 0)
            pygame.draw.ellipse(self.surface, ring_color, bounding_box, self.node_thickness)

            # TODO: Draw node's text
