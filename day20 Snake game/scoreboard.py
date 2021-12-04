from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.speed('fastest')
        self.score = 0
        self.highscore = 0
        self.color('white')
        self.goto(-10, 280)
        self.display_score()

    def write_highscore(self):
        with open("data.txt", 'w') as data:
            data.write(str(self.highscore))

    def read_highscore(self):
        with open("data.txt",'r') as data:
            return int(data.read())


    def increase_score(self):
        self.score += 1

    def display_score(self):
        self.clear()
        self.write(arg=f"Score : {self.score} Highscore: {self.read_highscore()}", move=False, align='center', font=('Arial', 15, 'normal'))

    def reset(self):
        if self.score > self.read_highscore():
            self.highscore = self.score
            self.write_highscore()
        self.score = 0

