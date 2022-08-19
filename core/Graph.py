from __future__ import annotations
from typing import TextIO

from core.Node import Node
from core.Colours import Colour, parse_colour

import json
import pygame


class Graph:
    """Stores a set of nodes, and colour information (if loaded from a JSON file)"""

    nodes:   list[Node]         # List of nodes parsed from JSON file
    colours: dict[str, Colour]  # Table of colours parsed from JSON file

    def __init__(self, file: str | TextIO, font: pygame.font.Font):
        self.nodes = []
        self.colours = {}
        if file:
            # Open file (supports file path, pointer, and JSON string)
            if file is TextIO:
                data = json.load(file)
            elif file[0] == '{':
                data = json.loads(file)
            else:
                data = json.load(open(file, 'r', encoding='utf-8'))

            self.colours = {
                key: parse_colour(value)
                for key, value in data.get('colours', []).items()
            }
            self.init_nodes(data['nodes'], font, self.colours)

    def init_nodes(self, data: dict, font: pygame.font.Font, colours: dict[str, Colour]) -> None:
        """Set up node and connection data from a dict (loaded from project-list JSON file)"""

        # Set up nodes
        for node_name, node in data.items():
            description = node.get('description', '')
            status = node.get('status', '')
            n = Node(node_name, description, status)
            self.add_node(n)

        # Set up connections
        for source, node in data.items():
            deps = node.get('deps', []) + node.get('dependencies', [])
            for dest in deps:
                self.add_connection(source, dest)

        # Finish setting up nodes
        for node in self.nodes:
            if not node.is_dependency_satisfied():
                node.status = 'missing deps'
            node.pre_render(font, colours)

    def add_node(self, node: Node) -> bool:
        """Adds a node to the graph's node-list"""
        if node not in self.nodes:
            self.nodes.append(node)
            return True
        return False

    def remove_node(self, _node: str | Node) -> bool:
        """Removes a node from the graph's node-list, severing any connections it has"""
        node = self.find_node(_node)
        if node:
            # Remove connections
            for node2 in node.dependencies:
                self.remove_connection(node, node2)
            for node2 in node.dependants:
                self.remove_connection(node2, node)
            # Remove node
            self.nodes.remove(node)
            return True
        return False

    def add_connection(self, _source: str | Node, _dest: str | Node) -> bool:
        """Creates a connection between 2 nodes in the graph's node-list"""
        source = self.find_node(_source)
        dest = self.find_node(_dest)
        if source and dest:
            source.dependencies.add(dest)
            dest.dependants.add(source)
            return True
        return False

    def remove_connection(self, _source: str | Node, _dest: str | Node) -> bool:
        """Removes a connection between 2 nodes in the graph's node-list"""
        source = self.find_node(_source)
        dest = self.find_node(_dest)
        if source and dest:
            source.dependencies.remove(dest)
            dest.dependants.remove(source)
            return True
        return False

    def find_node(self, node: str | Node) -> Node | None:
        """Convenience function for managing nodes by name.
        Searches the node-list if the input is a string.
        May return None if it can't find the requested node."""
        if node is Node:
            return node
        for n in self.nodes:
            if n.name == node:
                return n
