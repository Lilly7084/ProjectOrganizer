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

            self.init_nodes(data['nodes'], font)
            self.colours = {
                key: parse_colour(value)
                for key, value in data.get('colours', []).items()
            }

    def init_nodes(self, data: dict, font: pygame.font.Font) -> None:
        """Set up node and connection data from a dict (loaded from project-list JSON file)"""

        # Set up nodes
        for node_name, node in data.items():
            description = node.get('description', '')
            status = node.get('status', '')
            n = Node(node_name, description, status)
            n.pre_render(font)
            self.add_node(n)

        # Check node dependencies
        for node in self.nodes:
            if not node.is_dependency_satisfied():
                node.status = 'missing deps'

        # Set up connections
        for source, node in data.items():
            deps = node.get('deps', []) + node.get('dependencies', [])
            for dest in deps:
                self.add_connection(source, dest)

    def add_node(self, node: Node) -> None:
        """Adds a node to the graph's node-list"""
        if node not in self.nodes:
            self.nodes.append(node)

    def remove_node(self, _node: str | Node) -> None:
        """Removes a node from the graph's node-list, severing any connections it has"""
        node = self.find_node(_node)
        if node:
            # Remove connections
            for node2 in node.dependencies:
                self.remove_connection(node, node2)
            for node2 in node.dependants:
                self.remove_connection(node2, node)
            self.nodes.remove(node)

    def add_connection(self, _source: str | Node, _dest: str | Node) -> None:
        """Creates a connection between 2 nodes in the graph's node-list"""
        source = self.find_node(_source)
        dest = self.find_node(_dest)
        if source and dest:
            source.dependencies.add(dest)
            dest.dependants.add(source)
        # TODO: Warning message for failed connections?

    def remove_connection(self, _source: str | Node, _dest: str | Node) -> None:
        """Removes a connection between 2 nodes in the graph's node-list"""
        source = self.find_node(_source)
        dest = self.find_node(_dest)
        if source and dest:
            # TODO: Check for dangling / half connections?
            source.dependencies.remove(dest)
            dest.dependants.remove(source)

    def find_node(self, node: str | Node) -> Node | None:
        """Convenience function for managing nodes by name.
        Searches the node-list if the input is a string.
        May return None if it can't find the requested node."""
        if node is Node:
            return node
        for n in self.nodes:
            if n.name == node:
                return n
