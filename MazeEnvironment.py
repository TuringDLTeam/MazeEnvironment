from Environment import Environment
from MazeMonitor import MazeMonitor
from VertexGraph import VertexGraph
from utils import generate_maze


class MazeEnvironment(Environment):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

        paths, walls = generate_maze(width, height)
        self.__monitor = MazeMonitor(width, height, walls)

        self.__position = (0, 0)
        self.__goal_position = (self.__width - 1, self.__height - 1)
        self.__transition_graph = VertexGraph.from_edge_graph(paths, self.__width * self.__height)

    @property
    def state(self):
        return self.__monitor.image

    def reset(self):
        paths, walls = generate_maze(self.__width, self.__height)
        self.__monitor = MazeMonitor(self.__width, self.__height, walls)

        self.__transition_graph = VertexGraph.from_edge_graph(paths)

    def __get_new_position(self, action):
        x, y = self.__position

        if action == 0:  # Up
            y = max(0, y - 1)
        elif action == 1:  # Down
            y = min(self.__width - 1, y + 1)
        elif action == 2:  # Right
            x = min(self.__height - 1, x + 1)
        elif action == 3:  # Left
            x = max(0, x - 1)

        return x, y

    def step(self, action):
        new_pos = self.__get_new_position(action)
        # print(new_pos)
        self.__position = new_pos
        self.__monitor.move_agent(new_pos)

        if new_pos == self.__goal_position:
            return 100, self.__monitor.image, True, None

        return -1, self.__monitor.image, False, None

    def end(self):
        pass
