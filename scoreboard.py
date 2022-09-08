from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score_1 = 0
        self.score_2 = 0
        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto(0, 265)
        self.write(f'{self.score_1} Score {self.score_2}', align='center', font=('Courier', 24, 'normal'))

    def increase_score_1(self):
        self.score_1 += 1
        self.clear()
        self.write(f'{self.score_1} Score {self.score_2}', align='center', font=('Courier', 24, 'normal'))

    def increase_score_2(self):
        self.score_2 += 1
        self.clear()
        self.write(f'{self.score_1} Score {self.score_2}', align='center', font=('Courier', 24, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        if self.score_1 > self.score_2:
            self.write(f'Player 1 Wins!', align='center', font=('Courier', 24, 'normal'))
        else:
            self.write(f'Player 2 Wins!', align='center', font=('Courier', 24, 'normal'))


class DashedLine(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0, -280)
        self.setheading(90)
        while self.ycor() <= 270:
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)
