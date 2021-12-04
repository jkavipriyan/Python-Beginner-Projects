import random
from turtle import Turtle


class Ball:
    def __init__(self):
        self.balll = []
        self.make_ball()
        self.ball = self.balll[0]

    def make_ball(self):
        ball = Turtle()
        ball.penup()
        ball.shape('square')
        ball.color('white')
        ball.speed('normal')
        self.balll.append(ball)

    def set_heading(self):
        if 90 >= self.ball.heading() >= 0:
            self.ball.setheading(self.ball.heading() + 100)
        if 180 <= self.ball.heading() <= 270:
            self.ball.setheading(self.ball.heading() - 120)
        elif (270 < self.ball.heading() <= 360) or (180 > self.ball.heading() > 90):
            self.ball.setheading(self.ball.heading() + 90)

    def move_ball(self):
        self.ball.forward(20)

    def reflect(self):
        self.ball.setheading(self.ball.heading() - 180 + random.randint(-60, 60))
