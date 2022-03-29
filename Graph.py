class Graph:
    def __init__(self, nodes=0):
        self.__count_of_nodes = nodes
        self.__edge_dict = {}

    def add_node(self, count=1):
        self.__count_of_nodes += count

    @property
    def nodes(self):
        return self.__count_of_nodes

    def __str__(self):
        return f'Graph(\n\t#Nodes: {self.__count_of_nodes},\t#Edges: {len(self.__edge_dict.keys())}\n)'
