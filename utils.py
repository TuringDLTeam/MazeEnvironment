from EdgeGraph import EdgeGraph


def initialize_grid_graph(width, height):
    count = width * height

    graph = EdgeGraph(count)

    for head in range(count):
        for tail in range(head + 1, count):
            # print(head, tail)
            head_y, head_x = divmod(head, width)
            tail_y, tail_x = divmod(tail, width)

            if (head_x - tail_x == 1 and head_y == tail_y) or \
                    (head_x - tail_x == -1 and head_y == tail_y) or \
                    (head_x == tail_x and head_y - tail_y == 1) or \
                    (head_x == tail_x and head_y - tail_y == -1):
                graph.add_edge(head, tail)

    return graph
