#!/usr/bin/env python3
import json
import subprocess
import sys


def main():
    if len(sys.argv) != 2:
        print(f"Syntax: {sys.argv[0]} <projects.json file>")
        return

    with open(sys.argv[1], 'r') as file_ptr:
        file_data = json.load(file_ptr)
        c1 = file_data.get('colors', {})
        c2 = file_data.get('colours', {})
        colours = {**c1, **c2}
        nodes_raw = file_data['nodes']

    # Convert data to node-list and edge-list
    nodes = []
    name_to_index = {}
    named_edges = []
    for num, (key, value) in enumerate(nodes_raw.items()):
        name_to_index[key] = num
        nodes.append({
            'text': key,
            'notes': value.get('notes', ''),
            'status': value.get('status', 'available')
        })
        for dep in value['deps']:
            named_edges.append((dep, key))  # dep -[color]-> key

    # Resolve indices in edge-list
    edges = [
        (name_to_index[start], name_to_index[end])
        for (start, end) in named_edges
    ]

    # Check for missing dependencies
    for start, end in edges:
        if nodes[start]['status'] != 'completed':
            nodes[end]['status'] = 'missing deps'

    result = ""  # Buffer to hold generated D2 code

    # Add edges to output code
    for start, end in edges:
        colour = colours[nodes[start]['status']]
        result += f"{start} -> {end}: {{style.stroke: {colour}}}\n"
    result += "\n"

    # Add nodes to output code
    for num, node in enumerate(nodes):
        result += f"{num}: {node['text']}\n"
        result += f"{num}.style.stroke: {colours[node['status']]}\n"
        result += f"{num}.style.stroke-width: 8\n"
    result += "\n"

    pipe = subprocess.Popen(
        ['d2', '-l', 'elk', '-'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)
    out = pipe.communicate(input=result.encode('utf-8'))[0]

    out_path = sys.argv[1].replace('.json', '.svg')
    with open(out_path, 'wb') as file_ptr:
        file_ptr.write(out)


if __name__ == '__main__':
    main()
