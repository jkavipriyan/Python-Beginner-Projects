import turtle
from turtle import Turtle, Screen
import random
turtle.colormode(255)

def random_color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


spiry = Turtle()


spiry.speed("fastest")


for _ in range(36):
    spiry.pencolor(random_color())
    spiry.circle(100)
    spiry.left(10)

screen = Screen()
screen.exitonclick()
