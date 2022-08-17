from core.Graph import Graph
from positioners.Positioner import Positioner

import random


class RandomPositioner(Positioner):
    """Randomly positions nodes around the screen"""

    def place_graph(self, graph: Graph) -> None:
        for node in graph.nodes:
            node.position_x = int(random.random() * self.width)
            node.position_y = int(random.random() * self.height)
