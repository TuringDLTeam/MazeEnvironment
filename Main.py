from EdgeGraph import EdgeGraph
from utils import initialize_grid_graph


def main():
    pass


def graph_basic_test():
    graph = EdgeGraph(10)
    print(graph)

    graph.add_node(2)
    print(graph)


def test_grid_graph():
    graph = initialize_grid_graph(4, 3)
    print(graph)

    for number, edge in graph.edges.items():
        print(number, edge)


if __name__ == '__main__':
    # graph_basic_test()
    test_grid_graph()
