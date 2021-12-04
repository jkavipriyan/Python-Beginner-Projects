from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed('fastest')
        self.color('yellow')
        self.refresh()

    def refresh(self):
        self.goto(x=random.randint(-270, 270), y=random.randint(-270, 270))
