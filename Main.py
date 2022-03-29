from EdgeGraph import EdgeGraph
from MatrixImage import MatrixImage
from utils import initialize_grid_graph, generate_maze

import matplotlib.pyplot as plt


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

    print(graph.edge_list)


def test_maze_generator():
    print(generate_maze(10, 10))


def test_matrix_image():
    image = MatrixImage(10, 12)

    plt.imshow(image.image)
    plt.show()

    plt.imshow(image.image)
    plt.pause(.001)
    for i in range(10):
        for j in range(12):
            print(i, j)
            image.fill(i, j, (0, 1, 1))
            plt.imshow(image.image)
            plt.pause(.001)
    plt.show()


if __name__ == '__main__':
    # graph_basic_test()
    # test_grid_graph()
    # test_maze_generator()
    test_matrix_image()
