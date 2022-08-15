from Graph import Graph
from positioners.RandomPositioner import RandomPositioner


def main():
    g = Graph('./projects.json')
    rp = RandomPositioner()
    rp.place_graph(g)


if __name__ == '__main__':
    main()
