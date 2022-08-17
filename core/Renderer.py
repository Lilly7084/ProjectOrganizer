from core.Graph import Graph

import pygame


class Renderer:

    def __init__(self, width: int, height: int, line_thickness: int,
                 node_thickness: int, font: pygame.font.Font):
        pygame.init()
        self.width = width
        self.height = height
        self.line_thickness = line_thickness
        self.node_thickness = node_thickness
        self.font = font
        self.surface = pygame.Surface((width, height))
        self.surface.fill((255, 255, 255))

    def render(self, graph: Graph) -> None:
        """Draws a graph to the renderer's surface object.
        This function only needs to be called once, since the renderer has its own surface,
        which can be blitted to the window surface once per frame."""

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
            node.draw(self.surface, self.font, self.node_thickness)

    def show(self, surface: pygame.Surface) -> None:
        """Blits the renderer surface onto another surface"""
        surface.blit(self.surface, (0, 0))

    def export(self, file_path: str) -> None:
        """Saves the contents of the renderer surface to an image"""
        # TODO: Name hint 'jpg' might be expected to be 'jpeg'
        name_hint = file_path.split('.')[-1]
        with open(file_path, 'wb') as file_ptr:
            pygame.image.save(self.surface, file_ptr, name_hint)
