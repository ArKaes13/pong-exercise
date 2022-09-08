from turtle import Turtle
STARTING_POSITIONS = [(350, 0), (-350, 0)]


class Paddle:

    def __init__(self):
        self.paddles = []
        self.create_paddles()
        self.player_1 = self.paddles[1]
        self.player_2 = self.paddles[0]

    def create_paddles(self):
        for position in STARTING_POSITIONS:
            new_paddle = Turtle('square')
            new_paddle.color('white')
            new_paddle.penup()
            new_paddle.turtlesize(5, 1)
            new_paddle.goto(position)
            self.paddles.append(new_paddle)

    def move_up_1(self):
        if self.player_1.ycor() < 240:
            new_y = self.player_1.ycor() + 20
            self.player_1.goto(self.player_1.xcor(), new_y)

    def move_up_2(self):
        if self.player_2.ycor() < 240:
            new_y = self.player_2.ycor() + 20
            self.player_2.goto(self.player_2.xcor(), new_y)

    def move_down_1(self):
        if self.player_1.ycor() > -240:
            new_y = self.player_1.ycor() - 20
            self.player_1.goto(self.player_1.xcor(), new_y)

    def move_down_2(self):
        if self.player_2.ycor() > -240:
            new_y = self.player_2.ycor() - 20
            self.player_2.goto(self.player_2.xcor(), new_y)
