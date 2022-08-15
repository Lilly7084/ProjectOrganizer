from Graph import Graph
from positioners.Positioner import Positioner

import random


class RandomPositioner(Positioner):

    def place_graph(self, graph: Graph) -> None:
        for node in graph.nodes:
            node.position_x = int(random.random() * self.width)
            node.position_y = int(random.random() * self.height)
