from core.Graph import Graph
from core.Node import Node
from positioners.Positioner import Positioner


class TieredPositioner(Positioner):
    """Organizes a graph into dependency layers, and positions its nodes so the layers are stacked.
    'Dependency layers' are groups of nodes which depend only on the nodes in previous layers."""

    offset: tuple[int, int]   # How much space to put between nodes and the edge of the surface
    spacing: tuple[int, int]  # How much space to put between nodes
    layers: list[list[Node]]  # The dependency layers, useful for subclasses

    def __init__(self, offset: tuple[int, int], spacing: tuple[int, int]):
        super().__init__()
        self.offset = offset
        self.spacing = spacing
        self.layers = []

    def place_graph(self, graph: Graph) -> tuple[int, int]:
        self.layers = self.sort_layers(graph.nodes)
        self.place_layers(self.layers, self.offset, self.spacing)

        # Calculate positions
        def layer_width(layer):
            node = layer[-1]
            return node.position_x + node.width / 2

        def layer_height(layer):
            return max(map(lambda n: (n.position_y + n.height / 2), layer))

        width = max(map(layer_width, self.layers)) + self.offset[0]
        height = layer_height(self.layers[-1]) + self.offset[1]

        return width, height

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
    def place_layers(layers: list[list[Node]], offset: tuple[int, int], spacing: tuple[int, int]) -> None:
        """Sets the node positions for a list of dependency layers"""
        pos_y = offset[1]
        for (row, layer) in enumerate(layers):
            pos_x = offset[0]
            height = 0
            for (column, node) in enumerate(layer):
                node.position_x = pos_x + node.width / 2
                node.position_y = pos_y + node.height / 2
                pos_x += node.width + spacing[0]
                height = max(height, node.height)
            pos_y += height + spacing[1]
