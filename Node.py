from __future__ import annotations


class Node:

    def __init__(self, name: str = '', description: str = '', status: str = ''):
        self.name = name or ''  # The project's name, shown in the render
        self.description = description or ''  # A brief description of this project
        self.status = status or ''  # Current status of this project
        self.dependencies = set()  # Nodes which 'self' has as dependencies
        self.dependants = set()  # Nodes with 'self' as a dependency
        self.position_x = 0
        self.position_y = 0  # Coordinates range from 0 to 1!

    def __repr__(self):
        return "Node.Node(name={}, description={}, status={}, dependencies={}, position_x={}, position_y={})".format(
            self.name.__repr__(), self.description.__repr__(), self.status.__repr__(),
            self.dependencies, self.position_x.__repr__(), self.position_y.__repr__()
        )
