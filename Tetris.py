import pygame
import random

colors = [
    (0, 0, 0),
    (120, 37, 179),
    (100, 179, 179),
    (80, 34, 22),
    (80, 134, 22),
    (180, 34, 22),
    (180, 34, 122),
]


class block:
    x = 0
    y = 0

    blocke = [
        [[1, 5, 9, 13], [4, 5, 6, 7]],
        [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],
        [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],
        [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],
        [[1, 2, 5, 6]],
    ]

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.type = random.randint(0, len(self.blocke) - 1)
        self.color = random.randint(1, len(colors) - 1)
        self.rotation = 0

    def image(self):
        return self.blocke[self.type][self.rotation]

    def rotate(self):
        self.rotation = (self.rotation + 1) % len(self.blocke[self.type])


class Tetris:

    score = 0
    state = "start"
    field = []
    height = 0
    width = 0
    x = 100
    y = 60
    zoom = 20
    block = None

    def __init__(self, height, width):
        self.height = height
        self.width = width
        for i in range(height):
            new_line = []
            for j in range(width):
                new_line.append(0)
            self.field.append(new_line)

    def new_block(self):
        self.block = block(3, 0)

    def intersects(self):
        intersection = False
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.block.image():
                    if i + self.block.y > self.height - 1 or \
                            j + self.block.x > self.width - 1 or \
                            j + self.block.x < 0 or \
                            self.field[i + self.block.y][j + self.block.x] > 0:
                        intersection = True
        return intersection

    def break_lines(self):
        lines = 0
        for i in range(1, self.height):
            zeros = 0
            for j in range(self.width):
                if self.field[i][j] == 0:
                    zeros += 1
            if zeros == 0:
                lines += 1
                for i1 in range(i, 1, -1):
                    for j in range(self.width):
                        self.field[i1][j] = self.field[i1 - 1][j]
        self.score += lines ** 2

    def go_space(self):
        while not self.intersects():
            self.block.y += 1
        self.block.y -= 1
        self.freeze()

    def go_down(self):
        self.block.y += 1
        if self.intersects():
            self.block.y -= 1
            self.freeze()

    def freeze(self):
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.block.image():
                    self.field[i + self.block.y][j + self.block.x] = self.block.color
        self.break_lines()
        self.new_block()
        if self.intersects():
            game.state = "gameover"

    def go_side(self, dx):
        old_x = self.block.x
        self.block.x += dx
        if self.intersects():
            self.block.x = old_x

    def rotate(self):
        old_rotation = self.block.rotation
        self.block.rotate()
        if self.intersects():
            self.block.rotation = old_rotation




 # Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

size = (400, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Tetris")



#   font = pygame.font.SysFont('Calibri', 25, True, False)
#  font1 = pygame.font.SysFont('Calibri', 65, True, False)
# text = font.render("Score: " + str(game.score), True, BLACK)
#text_game_over = font1.render("Game Over :( ", True, (255, 0, 0)
