from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard, DashedLine
import time


# Set various display settings.
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

paddle = Paddle()
ball = Ball()
scoreboard = ScoreBoard()
dashed_line = DashedLine()

# Allows control of the paddles and stops them at the boundary.
screen.listen()
screen.onkeypress(paddle.move_up_1, 'w')
screen.onkeypress(paddle.move_down_1, 's')
screen.onkeypress(paddle.move_up_2, 'Up')
screen.onkeypress(paddle.move_down_2, 'Down')

game_over = False
while not game_over:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detect collision with wall.
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddles.
    if ball.distance(paddle.player_1) < 50 and ball.xcor() < -320 or ball.distance(paddle.player_2) < 50 and \
            ball.xcor() > 320:
        ball.bounce_x()

    # Detect if the ball went out of bounds, reset the ball in an opposite direction, and add score to correct player.
    if ball.xcor() > 380:
        scoreboard.increase_score_1()
        ball.reset_position()

    if ball.xcor() < -380:
        scoreboard.increase_score_2()
        ball.reset_position()

    if scoreboard.score_1 == 5 or scoreboard.score_2 == 5:
        game_over = True
        scoreboard.game_over()

screen.exitonclick()
