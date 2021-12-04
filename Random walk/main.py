import turtle
from turtle import Turtle, Screen
import random

tom = Turtle()
tom.pensize(5)
tom.speed(10)
directions = [tom.forward, tom.backward]
angle = [tom.left, tom.right]
angle_values = [90, 180, 270, 360]
turtle.colormode(255)


def random_color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


def walk(directions, angle):
    random.choice(directions)(15)
    random.choice(angle)(random.choice(angle_values))


for _ in range(50):
    walk(directions, angle)
    tom.pencolor(random_color())

screen = Screen()
screen.exitonclick()
