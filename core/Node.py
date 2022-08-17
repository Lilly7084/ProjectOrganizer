from __future__ import annotations

from core import DrawingUtils

import pygame


class Node:
    """Stores all the information for a single node; name, description, status,
    dependencies, dependants, position, size, etc."""

    name:         str             # The node name, shown in the graph
    description:  str             # A short description of the project
    status:       str             # Status string (key for Graph.colours)
    dependencies: set[Node]       # Nodes which this has as dependencies
    dependants:   set[Node]       # Nodes which have this as a dependency
    text_surf:    pygame.Surface  # Surface containing pre-rendered text
    position_x:   int             # Where on the surface the node will appear (X)
    position_y:   int             # Where on the surface the node will appear (Y)
    width:        int             # How large the node must be to fit its text (X)
    height:       int             # How large the node must be to fit its text (Y)

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

    def pre_render(self, font: pygame.font.Font) -> None:
        """Rendering stage 1: Sets up the node to be drawn to a surface"""
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
