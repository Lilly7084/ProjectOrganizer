from Graph import Graph


def main():
    g = Graph('./projects.json')
    print()
    print(g.find_node('hydroponics'))


if __name__ == '__main__':
    main()
