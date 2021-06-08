import pygame
import random


class Block:
    x = 0
    y = 0

    Block = [                         #Hier werden die einzelnen Figuren in einer Liste definiert (4x4 Feld)
        [[4, 5, 9, 10], [2, 6, 5, 9]],                                  #Schlangenblock, gedreht
        [[6, 7, 9, 10], [1, 5, 6, 10]],                                 #Schlangenblock gespiegelt, gedreht
        [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],      #L Block gedreht
        [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],    #L Block gespiegelt, gedreht
        [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],       #T Block gespiegelt, gedreht
        [1, 2, 5, 6]                                                    #2x2 Block
        ]

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.type = random.randint(0, len(self.Block) - 1)
        self.rotation = 0

    def image(self):
        return self.Block[self.type][self.rotation]

    def rotate(self):

