

import random
from constants import *

class Rectangle:

    def __init__(self):
        """Creates a new Rectangle"""
        self.height = (random.random())*(HEIGHT- MIN_HEIGHT) + MIN_HEIGHT

    @classmethod
    def rectanglesSpawn(cls):
        """ Spawns all the rectangles and returns the list of all the rectangles """
        rectangles = []
        for i in range(NO_OF_RECTANGLES):
            rectangle = Rectangle()
            rectangles.append(rectangle)
        return rectangles
        