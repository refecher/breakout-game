import random
from turtle import Turtle

option_colors = ['green', 'orange', 'yellow', 'pink', 'purple', 'gold', 'gray', 'brown', 'white']


# class Blocks(Turtle):
#     def __init__(self, x, y):
#         super().__init__()
#         self.shape("square")
#         self.penup()
#         self.shapesize(stretch_wid=2.5, stretch_len=5.5)
#         self.colors = ["red", "blue", "yellow", "green", "cyan", "orange", "purple"]
#         self.color(random.choice(self.colors))
#         self.goto(x, y)


class Blocks:
    def __init__(self, x, y):
        self.bx, self.by = x, y
        self.blocks_list = []
        self.create_blocks()

    def create_blocks(self):
        for _ in range(5):
            for _ in range(12):
                self.add_block()
                self.bx += 115
            self.bx = -633
            self.by -= 55

    def add_block(self):
        # Variables
        colors = ["cyan", "red", "green", "orange", "yellow", "pink", "purple", "gold", "brown", "white"]

        # Config turtle
        block = Turtle("square")
        block.penup()
        block.shapesize(stretch_wid=2.5, stretch_len=5.5)
        block.color(random.choice(colors))
        block.goto(self.bx, self.by)
        self.blocks_list.append(block)

    def reset(self):
        self.blocks_list.clear()
        self.bx, self.by = -633, 280
        self.create_blocks()

