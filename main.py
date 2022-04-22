from turtle import Screen
from ball import Ball
from paddle import Paddle
from scoreboard import ScoreBoard
from border import GameBorder
from blocks import Blocks
import time

# Variables
BALL_SIZE = 20
BORDER_WIDTH, BORDER_HEIGHT = 1400, 900
INITIAL_PADDLE_COR = (0, -430)
PADDLE_STRETCH_WID, PADDLE_STRETCH_LEN = 1, 20
paddle_width, paddle_height = (20 * PADDLE_STRETCH_LEN), (20 * PADDLE_STRETCH_WID)
BLOCK_STRETCH_WID, BLOCK_STRETCH_LEN = 2.5, 5.5
block_width, block_height = (20 * BLOCK_STRETCH_LEN), (20 * BLOCK_STRETCH_WID)
# 20 is the normal size of the turtle, multiply it for the desired stretch to have the actual size

# Config screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=1500, height=1000)
screen.title("The Breakout Game")
screen.tracer(0)  # check what it means

# Create turtles
scoreboard = ScoreBoard()
ball = Ball(BORDER_WIDTH, BORDER_HEIGHT)
paddle = Paddle(INITIAL_PADDLE_COR, BORDER_WIDTH, paddle_width)
border = GameBorder(BORDER_WIDTH, BORDER_HEIGHT)
blocks = Blocks(-633, 280)

# Add the functionality to the paddles
screen.listen()
screen.onkeypress(fun=paddle.go_left, key="Left")
screen.onkeypress(fun=paddle.go_right, key="Right")
# screen.onkeyrelease(fun=ball.move, key="space")

## TODO 1 - Have the ball starting at the middle of the paddle and the space key starting the movement of the ball

game_is_on = True
while game_is_on:
    #
    screen.update()
    ball.move()
    time.sleep(0.03)

    # Detect collision with the paddle
    if ball.distance(paddle) < 220 and ball.ycor() == -410:
        ball.dy *= -1

    # Detect collision with the blocks
    for block in blocks.blocks_list:
        if ball.is_collision(block, BALL_SIZE, block_width, block_height):
            scoreboard.track_point()
            ball.dy *= -1
            block.hideturtle()
            # Fix problem with last block
            blocks.blocks_list.remove(block)

    # Detect collision with the bottom and keep track of the lives
    if ball.y <= -BORDER_HEIGHT / 2.0 + 10:
        ball.x = 0
        ball.y = -410
        scoreboard.track_life()

    # Detect lives
    if scoreboard.lives == 0:
        blocks.reset()
        scoreboard.reset()

    # Detect game over
    if not blocks.blocks_list:
        # Send ball back to beginning
        ball.x = 0
        ball.y = -410

        blocks.reset()

screen.exitonclick()
