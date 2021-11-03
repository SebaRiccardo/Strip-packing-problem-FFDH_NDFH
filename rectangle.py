import random
import numpy as np

class Rectangle:


    def __init__(self,width,height,number):
        self.width = width
        self.height = height
        self.number = number

    def __str__(self):
        return "Rectangle: number= %s width= %s height= %s" % (self.number,self.width,self.height)

    def get_width(self): return self.width

    def get_height(self): return self.height

    def get_number(self): return self.number


# Creates rectangles of width (10,50) and height (10,75)
def generate_rectangles(number_of_rectangles):

        #Use seed only for debug
        # np.random.seed(1)
        return [Rectangle(np.random.randint(10,51),np.random.randint(10,76),i) for i in range(number_of_rectangles)]
