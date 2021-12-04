from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self,x):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.penup()
        self.color('white')
        self.speed('fastest')
        self.goto(x= x, y=340 )
        self.write_score()

    def increase_score(self):
        self.score += 1

    def write_score(self):
        self.clear()
        self.write(arg=self.score, move=False, align='center', font=('Arial', 45, 'normal'))

    def game_over(self):
        self.clear()
        self.home()
        self.write(arg='Game over', move=False, align='center', font=('Arial', 45, 'normal'))