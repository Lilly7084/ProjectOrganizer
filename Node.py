from __future__ import annotations

import pygame


class Node:

    def __init__(self, name: str = '', description: str = '', status: str = ''):
        self.name = name  # The project's name, shown in the render
        self.description = description  # A brief description of this project
        self.status = status  # Current status of this project
        self.dependencies = set()  # Nodes which 'self' has as dependencies
        self.dependants = set()  # Nodes with 'self' as a dependency
        self.position_x = 0
        self.position_y = 0  # Coordinates range from 0 to 1!
        # TODO: Calculate node size instead of hard-coding it
        self.width = 48
        self.height = 24

    def draw(self, surface: pygame.Surface, node_thickness: int = 1):
        """Draws the node to a PyGame surface object"""

        # Find bounding box
        pos_x = self.position_x - self.width / 2
        pos_y = self.position_y - self.height / 2
        bounding_box = pygame.Rect(pos_x, pos_y, self.width, self.height)

        # Draw node outline
        ring_color = (0, 0, 0)
        pygame.draw.ellipse(surface, (255, 255, 255), bounding_box, 0)
        pygame.draw.ellipse(surface, ring_color, bounding_box, node_thickness)

        # TODO: Draw node's text

    def __repr__(self):
        pos_data = "position_x={}, position_y={}, width={}, height={}".format(
                self.position_x, self.position_y, self.width, self.height)
        return "Node.Node(name={}, description={}, status={}, dependencies={}, {})".format(
            self.name.__repr__(), self.description.__repr__(), self.status.__repr__(),
            self.dependencies, pos_data
        )
