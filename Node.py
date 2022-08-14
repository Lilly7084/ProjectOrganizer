from __future__ import annotations


class Node:

    def __init__(self, name: str = '', description: str = '', status: str = ''):
        self.name = name or ''
        self.description = description or ''
        self.status = status or ''
        self.dependencies = set()
        self.position_x = 0
        self.position_y = 0  # Coordinates range from -1 to 1!

    def __repr__(self):
        return "Node.Node(name={}, description={}, status={}, dependencies={})".format(
            self.name.__repr__(), self.description.__repr__(), self.status.__repr__(), self.dependencies
        )
