from __future__ import annotations

from core import DrawingUtils

import pygame


class Node:
    """Stores all the information for a single node; name, description, status,
    dependencies, dependants, position, size, etc."""

    name: str
    description: str
    status: str
    dependencies: set[Node]
    dependants: set[Node]
    text_surf: pygame.Surface
    position_x: int
    position_y: int
    width: int
    height: int

    def __init__(self, name: str, description: str, status: str):
        # Strings
        self.name = self.unescape(name)
        self.description = self.unescape(description)
        self.status = self.unescape(status)
        # Links
        # TODO: Do we really need to store dependant nodes?
        self.dependencies = set()  # Nodes which 'self' has as dependencies
        self.dependants = set()  # Nodes which have 'self' as a dependency

    @staticmethod
    def unescape(s: str) -> str:
        # Source: https://thewebdev.info/2022/04/14/how-to-un-escape-a-backslash-escaped-string-with-python/
        return s.encode('raw_unicode_escape').decode('unicode_escape')

    def pre_render(self, font: pygame.font.Font):
        chars_per_line = 28
        self.text_surf = DrawingUtils.draw_text(self.name, chars_per_line, font, None, (0, 0))
        width, height = self.text_surf.get_size()
        oversize = 8
        self.width = width + oversize
        self.height = height + oversize

    def draw_node(self, surface: pygame.Surface, node_thickness: int) -> None:
        """Draws the node to a PyGame surface object"""

        # Draw node outline
        node_colour = (255, 0, 0)
        pos_x = self.position_x - self.width / 2
        pos_y = self.position_y - self.height / 2
        bounding_box = pygame.Rect(pos_x, pos_y, self.width, self.height)
        pygame.draw.rect(surface, (255, 255, 255), bounding_box, 0)
        pygame.draw.rect(surface, node_colour, bounding_box, node_thickness)

        # Draw text
        width, height = self.text_surf.get_size()
        pos_x = self.position_x - width / 2
        pos_y = self.position_y - height / 2
        surface.blit(self.text_surf, (pos_x, pos_y))

    def is_dependency_satisfied(self) -> bool:
        """Check if all dependencies for this node have been completed"""
        return all((dep.status == 'completed') for dep in self.dependencies)

    def __repr__(self):
        # TODO: Do we really need __repr__?
        pos_data = "position_x={}, position_y={}, width={}, height={}".format(
                self.position_x, self.position_y, self.width, self.height)
        return "Node.Node(name={}, description={}, status={}, dependencies={}, {})".format(
            self.name.__repr__(), self.description.__repr__(), self.status.__repr__(),
            self.dependencies, pos_data
        )
