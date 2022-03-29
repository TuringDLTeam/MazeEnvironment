class Graph:
    def __init__(self, nodes=0):
        self.__count_of_nodes = nodes
        self.__edges = 0
        self.__edge_dict = {}

    def add_node(self, count=1):
        self.__count_of_nodes += count

    def add_edge(self, head, tail):
        self.__edge_dict[self.__edges] = (head, tail)

    def remove_edge(self, edge):
        del self.__edges[edge]

    @property
    def nodes(self):
        return self.__count_of_nodes

    def __str__(self):
        return f'Graph(\n\t#Nodes: {self.__count_of_nodes},\t#Edges: {self.__edges}\n)'
