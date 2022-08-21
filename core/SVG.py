from core.Graph import Graph
from core.Node import Node


class SVGExporter:

    node_thickness: int
    line_thickness: int
    text_size: float
    invert: bool
    background: bool
    main: str
    alt: str

    def __init__(self, node_thickness: int, line_thickness: int,
                 text_size: float, invert: bool, background: bool) -> None:
        self.rect_thickness = node_thickness
        self.line_thickness = line_thickness
        self.text_size = text_size
        self.invert = invert
        self.enable_background = background
        self.main = '000000' if invert else 'ffffff'
        self.alt = 'ffffff' if invert else '000000'

    def get_xml(self, graph: Graph, width: int, height: int) -> str:
        nodes = "\n".join([self.node(node) for node in graph.nodes])

        edges_list = []
        for node in graph.nodes:
            for dep in node.dependants:
                edges_list.append(self.line(node.position_x, node.position_y, dep.position_x, dep.position_y))
        edges = "\n".join(edges_list)

        return "\n".join([self.header(width, height),
                          (self.background(width, height) if self.enable_background else ""),
                          edges,
                          nodes,
                          self.footer()
                          ])

    @staticmethod
    def header(width: int, height: int) -> str:
        return f"""<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg
   width="{width}px"
   height="{height}px"
   viewBox="0 0 {width} {height}"
   version="1.1"
   id="svg5"
   xmlns="http://www.w3.org/2000/svg"
   xmlns:svg="http://www.w3.org/2000/svg">
  <g>"""

    @staticmethod
    def footer() -> str:
        return """  </g>
</svg>"""

    def background(self, width: int, height: int) -> str:
        return f"""    <rect
       style="fill:#{self.main}"
       width="{width}"
       height="{height}"
       x="0"
       y="0" />"""

    def rect(self, width: int, height: int, x: int, y: int) -> str:
        return f"""    <rect
       style="fill:#{self.main};stroke:#{self.alt};stroke-width:{self.node_thickness}"
       width="{width}"
       height="{height}"
       x="{x}"
       y="{y}" />"""

    def line(self, start_x: int, start_y: int, end_x: int, end_y: int) -> str:
        return f"""    <path
       style="fill:#{self.main};stroke:#{self.alt};stroke-width:{self.line_thickness}"
       d="m {start_x},{start_y} {end_x},{end_y}"
       id="path551" />"""

    def text(self, x: int, y: int, content: str):
        return f"""    <text
       style="font-size:{self.text_size}px;fill:#{self.alt}"
       x="{x}"
       y="{y}">{content}</text>"""

    def node(self, node: Node):
        rect = self.rect(node.width, node.height, node.position_x, node.position_y)
        text = self.text(node.position_x, node.position_y, node.name)
        return rect + "\n" + text
