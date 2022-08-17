from core.Graph import Graph
from positioners.Positioner import Positioner

import random


class RandomPositioner(Positioner):
    """Randomly positions nodes around the screen"""

    def __init__(self, width: int = 640, height: int = 480):
        super().__init__()
        self.width = width
        self.height = height

    def place_graph(self, graph: Graph) -> tuple[int, int]:
        for node in graph.nodes:
            node.position_x = int(random.random() * self.width)
            node.position_y = int(random.random() * self.height)
        return self.width, self.height
