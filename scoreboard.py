from turtle import Turtle

INITIAL_SCORE = 0
INITIAL_LIVES = 3
FONT = ("courier", 40, "normal")
ALIGNMENT = "center"


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.goto(0, 420)
        self.hideturtle()
        self.color("white")
        self.score = INITIAL_SCORE
        self.lives = INITIAL_LIVES
        self.count_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = INITIAL_SCORE
        self.lives = INITIAL_LIVES
        self.count_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)

    def count_score(self):
        self.clear()
        self.write(arg=f"SCORE: {self.score}   HIGH SCORE: {self.high_score}   LIVES: {self.lives}", align=ALIGNMENT, font=FONT)

    def track_point(self):
        self.score += 1
        self.count_score()

    def track_life(self):
        self.lives -= 1
        self.count_score()