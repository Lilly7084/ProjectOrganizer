from __future__ import annotations

from core import DrawingUtils

import pygame


class Node:
    """Stores all the information for a single node; name, description, status,
    dependencies, dependants, position, size, etc."""

    def __init__(self, name: str, description: str, status: str, font: pygame.font.Font):
        # Strings
        self.name = name  # The project's name, shown in the render
        self.description = description  # A brief description of this project
        self.status = status  # Current status of this project
        # Links
        self.dependencies = set()  # Nodes which 'self' has as dependencies
        # TODO: Do we really need to store dependant nodes?
        self.dependants = set()  # Nodes which have 'self' as a dependency
        # Pre-render text surface (Surface size used as node size)
        chars_per_line = 28
        self.text_surf = DrawingUtils.draw_text(name, chars_per_line, font, None, (0, 0))
        width, height = self.text_surf.get_size()
        oversize = 8
        self.width = width + oversize
        self.height = height + oversize
        self.position_x = 0
        self.position_y = 0

    def draw_node(self, surface: pygame.Surface, font: pygame.font.Font, node_thickness: int):
        """Draws the node to a PyGame surface object"""

        # Find bounding box
        pos_x = self.position_x - self.width / 2
        pos_y = self.position_y - self.height / 2
        bounding_box = pygame.Rect(pos_x, pos_y, self.width, self.height)

        # Draw node outline
        ring_color = (0, 0, 0)
        pygame.draw.rect(surface, (255, 255, 255), bounding_box, 0)
        pygame.draw.rect(surface, ring_color, bounding_box, node_thickness)

        # Draw text
        width, height = self.text_surf.get_size()
        pos_x = self.position_x - width / 2
        pos_y = self.position_y - height / 2
        surface.blit(self.text_surf, (pos_x, pos_y))

    def is_dependency_satisfied(self) -> bool:
        """Check if all dependencies for this node have been completed"""
        return all((dep.status == 'completed') for dep in self.dependencies)

    def __repr__(self):
        pos_data = "position_x={}, position_y={}, width={}, height={}".format(
                self.position_x, self.position_y, self.width, self.height)
        return "Node.Node(name={}, description={}, status={}, dependencies={}, {})".format(
            self.name.__repr__(), self.description.__repr__(), self.status.__repr__(),
            self.dependencies, pos_data
        )
