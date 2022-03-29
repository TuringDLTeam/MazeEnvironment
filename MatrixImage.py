import numpy as np


class MatrixImage:
    def __init__(self, width, height, **kwargs):
        self.__width = width
        self.__height = height

        self.__scale_factor = kwargs.get('scale_factor', 10)
        self.__image = np.zeros((self.__height * self.__scale_factor, self.__width * self.__scale_factor, 3))

    def fill(self, x, y, color):
        start_x = x * self.__scale_factor
        start_y = y * self.__scale_factor
        end_x = start_x + self.__scale_factor
        end_y = start_y + self.__scale_factor

        self.__image[start_y:end_y, start_x:end_x] = color

    @property
    def image(self):
        return self.__image
