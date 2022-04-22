from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, coordinate, border_w, paddle_w):
        super().__init__()
        # Variables
        self.border_width = border_w
        self.paddle_width = paddle_w

        # Turtle config
        self.shape("square")
        self.color("blue")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=20)
        self.goto(coordinate)

    def go_right(self):
        # Only move paddle if it's not touching the border
        if self.xcor() <= (self.border_width / 2 - self.paddle_width / 2) - 25:
            new_x = self.xcor() + 45
            self.goto(new_x, self.ycor())

    def go_left(self):
        if self.xcor() >= -((self.border_width / 2 - self.paddle_width / 2) - 25):
            new_x = self.xcor() - 45
            self.goto(new_x, self.ycor())

    def border_check(self):
        # Check left and right border
        if self.xcor() >= self.border_width / 2.0 - 10:
            # Disable right button
            pass
        elif self.xcor() <= -self.border_width / 2.0 + 10:
            # Disable left button
            pass

