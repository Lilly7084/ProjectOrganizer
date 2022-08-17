from core.Graph import Graph


class Positioner:
    """A generic class for objects which set the positions of nodes"""

    def __init__(self, width: int = 640, height: int = 480):
        self.width = width
        self.height = height

    def place_graph(self, graph: Graph) -> None:
        """Sets the node positions for an entire graph"""
        pass
