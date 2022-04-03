

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
        
    @classmethod
    def bubble_sort(cls, i, j, rectangles):
        if i > 0: # Bubble sorting algorithm
            if j + 1 < i:
                    if rectangles[j].height > rectangles[j+1].height:
                        temp = rectangles[j+1]
                        rectangles[j+1] = rectangles[j]
                        rectangles[j] = temp
            else: # AT_RECTANGLE has reached NO_OF_RECTANGLES's value => sorting completed
                i -= 1
                j = -1 # putting it as -1 because the next statement "j += 1" increments it immediately
            j += 1
        return [i, j]
    
    @classmethod
    def bubble_sort2(cls, i, j, rectangles):
        if i < len(rectangles):
            if j > 0:
                if rectangles[j].height < rectangles[j-1].height:
                    temp = rectangles[j]
                    rectangles[j] = rectangles[j-1]
                    rectangles[j-1] = temp
            else:
                i += 1
                j = i + 1
            j -= 1


        return [i, j]