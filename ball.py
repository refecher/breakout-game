from turtle import Turtle


class Ball(Turtle):
    def __init__(self, border_w, border_h):
        super().__init__()
        # Variables
        self.border_width = border_w
        self.border_height = border_h
        self.player_lives = 3

        # Config Turtle
        self.color("gray")
        self.shape("circle")
        self.speed("fastest")
        self.penup()

        # x and y determine where the ball will come from (initial position)
        self.x = 0
        self.y = -410

        # delta determine the movement
        # try to find a way to start the movement randomly without affecting the speed
        self.dx = -8
        self.dy = 8

    def move(self):
        self.x += self.dx
        self.y += self.dy
        self.goto(self.x, self.y)
        self.border_check()

    def border_check(self):
        # Check left and right border
        if self.x >= self.border_width / 2.0 - 10 or self.x <= -self.border_width / 2.0 + 10:
            self.dx *= -1

        # Check top and bottom border
        if self.y >= self.border_height / 2.0 - 60 or self.y <= -self.border_height / 2.0 + 10:
            self.dy *= -1
            # if self.y <= -self.border_height / 2.0 + 10:
            #     # Restart the ball
            #     self.x = 0
            #     self.y = -410
            #     self.player_lives -= 1

    def is_collision(self, block, ball_size, block_width, block_height):
        # Size of the blocks
        # block_width, block_height = 110, 50
        # ball_size = 20
        return abs(self.xcor() - block.xcor()) < ball_size / 2 + block_width / 2 and \
               abs(self.ycor() - block.ycor()) < ball_size / 2 + block_height / 2