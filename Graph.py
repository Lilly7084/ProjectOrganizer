from __future__ import annotations
from typing import TextIO

from Node import Node

import json


class Graph:

    # TODO: make node list support arbitrarily many dimensions, to better organize node pointers.
    # This will be helpful when more advanced positioners are added.
    nodes: list[Node] = []

    # TODO: Store non-node data from init file (Keep original JSON dict, but discard node data?)

    def __init__(self, file: str | TextIO = None):
        if file:
            # Open file (supports file path, pointer, and JSON string)
            if file is TextIO:
                data = json.load(file)
            elif file[0] == '{':
                data = json.loads(file)
            else:
                data = json.load(open(file, 'r', encoding='utf-8'))

            # TODO: use color information from file

            # Set up nodes
            for node_name, node in data['nodes'].items():
                description = node['description'] if 'description' in node else ''
                status = node['status'] if 'status' in node else ''
                n = Node(name=node_name, description=description, status=status)
                self.add_node(n)

            # Set up connections
            for source, node in data['nodes'].items():
                deps_short = node['deps'] if 'deps' in node.keys() else []
                deps_long = node['dependencies'] if 'dependencies' in node.keys() else []
                for dest in (deps_short + deps_long):
                    self.add_connection(source, dest)

    def add_node(self, node: Node):
        if node not in self.nodes:
            self.nodes.append(node)

    # TODO: Add code to remove nodes

    def add_connection(self, source: str | Node, dest: str | Node):
        _source = self.find_node(source)
        _dest = self.find_node(dest)
        _source.dependencies.add(_dest)
        _dest.dependants.add(_source)

    # TODO: Add code to remove connections

    def find_node(self, node: str | Node) -> Node:
        if node is Node:
            return node
        for n in self.nodes:
            if n.name == node:
                return n
