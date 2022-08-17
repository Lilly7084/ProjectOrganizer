from core.Graph import Graph


class Positioner:
    """A generic class for objects which set the positions of nodes"""

    def __init__(self):
        pass

    def place_graph(self, graph: Graph) -> tuple[int, int]:
        """Sets the node positions for an entire graph.
        Returns the size of the surface necessary to contain the graph."""
        pass
