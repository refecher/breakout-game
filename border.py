from turtle import Turtle


class GameBorder(Turtle):
    def __init__(self, border_width, border_height):
        super().__init__()
        # Variables
        self.border_width = border_width
        self.border_height = border_height

        # Turtle config
        self.hideturtle()
        self.color("white")
        self.pensize(width=2)
        self.penup()

        self.draw_borders()

    def draw_borders(self):
        left = -self.border_width / 2
        right = self.border_width / 2
        top = (self.border_height / 2) - 50
        bottom = -self.border_height / 2

        self.goto(left, top)
        self.pendown()
        self.goto(right, top)
        self.goto(right, bottom)
        self.goto(left, bottom)
        self.goto(left, top)
        self.penup()
