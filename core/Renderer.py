from core.Graph import Graph

import pygame


class Renderer:

    surface: pygame.Surface  # The surface to render graphs onto
    line_thickness: int      # How thick connections should be drawn
    node_thickness: int      # How thick the node's rings should be drawn
    font: pygame.font.Font   # The font used for node labels

    def __init__(self, width: int, height: int, line_thickness: int,
                 node_thickness: int, font: pygame.font.Font):
        pygame.init()
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
        for node in graph.nodes:
            node.draw_connections(self.surface, self.line_thickness)

        # Draw nodes
        for node in graph.nodes:
            node.draw_node(self.surface, self.node_thickness)

    def show(self, surface: pygame.Surface) -> None:
        """Blits the renderer surface onto another surface"""
        surface.blit(self.surface, (0, 0))

    def export(self, file_path: str) -> None:
        """Saves the contents of the renderer surface to an image"""
        name_hint = file_path.split('.')[-1]
        with open(file_path, 'wb') as file_ptr:
            pygame.image.save(self.surface, file_ptr, name_hint)

    def export_svg(self, file_path: str, graph: Graph, text_size: int, invert=False, background=True) -> None:
        from SVG import SVGExporter
        exporter = SVGExporter(self.node_thickness, self.line_thickness, text_size, invert, background)
        open(file_path, "w").write(exporter.get_xml(graph, self.surface.get_width(), self.surface.get_height()))
