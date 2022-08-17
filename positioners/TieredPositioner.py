from core.Graph import Graph
from core.Node import Node
from positioners.Positioner import Positioner


class TieredPositioner(Positioner):
    """Organizes a graph into dependency layers, and positions its nodes so the layers are stacked.
    'Dependency layers' are groups of nodes which depend only on the nodes in previous layers."""

    layers: list[list[Node]] = []

    def place_graph(self, graph: Graph) -> tuple[int, int]:
        self.layers = self.sort_layers(graph.nodes)
        width = max(map(len, self.layers))
        height = len(self.layers)
        self.place_layers(self.layers, self.spacing)
        return width * self.spacing, height * self.spacing

    @staticmethod
    def sort_layers(nodes: list[Node]) -> list[list[Node]]:
        """Organizes a list of nodes into dependency layers"""
        to_eval = nodes.copy()  # Copy to avoid concurrent modification issues
        layers = []

        # Create a filter function to find available nodes
        def is_in_layer(n: Node) -> bool:
            return all(dep not in to_eval for dep in n.dependencies)

        # While there's still more nodes to evaluate:
        while to_eval:
            # Take all nodes that don't have unlisted dependencies
            layer = list(filter(is_in_layer, to_eval))
            # Store them as a new layer
            layers.append(layer)
            # Delete them from the evaluation queue
            for node in layer:
                to_eval.remove(node)

        return layers

    @staticmethod
    def place_layers(layers: list[list[Node]], spacing: int) -> None:
        """Sets the node positions for a list of dependency layers"""
        for (row, layer) in enumerate(layers):
            for (column, node) in enumerate(layer):
                node.position_x = spacing * (column + 0.5)
                node.position_y = spacing * (row + 0.5)
