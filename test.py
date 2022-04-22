from turtle import Turtle
import random

BORDER_WIDTH = 1400
BORDER_HEIGHT = 900


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("gray")
        self.shape("circle")
        self.speed(0)
        self.penup()

        # x and y determine where the ball will come from (initial position)
        self.x = 0
        self.y = -410

        # delta determine the movement
        # try to find a way to start the movement randomly without affecting the speed
        self.dx = -4
        self.dy = 4

        # size of the paddle
        self.width = 100
        self.height = 20

        print(self.dx, self.dy)

    def move(self):
        self.x += self.dx
        self.y += self.dy
        self.goto(self.x, self.y)
        self.border_check()

    def border_check(self):
        # Check left and right border
        if self.x >= BORDER_WIDTH / 2.0 - 10 or self.x <= -BORDER_WIDTH / 2.0 + 10:
            self.dx *= -1

        # Check top and bottom border
        if self.y >= BORDER_HEIGHT / 2.0 - 60 or self.y <= -BORDER_HEIGHT / 2.0 + 10:
            self.dy *= -1
            if self.y <= -BORDER_HEIGHT / 2.0 + 10:
                # Restart the ball
                self.x = 0
                self.y = -410

    def is_collision(self, block):
        # Size of the blocks
        block_width, block_height = 110, 50
        ball_size = 20
        return abs(self.xcor() - block.xcor()) < ball_size / 2 + block_width / 2 and \
               abs(self.ycor() - block.ycor()) < ball_size / 2 + block_height / 2