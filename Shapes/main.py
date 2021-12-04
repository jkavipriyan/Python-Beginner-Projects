from turtle import Turtle, Screen
import random

tim = Turtle()
colours = ['black', 'red', 'blue', 'yellow', 'coral', 'pink', 'green']
shapes = [3, 4, 5, 6, 7, 8, 9, 10]
angle = []
for _ in shapes:
    angle.append(360/_)
print(angle)
iterr1 = 0
iterr2 = 3

for _ in range(len(shapes)):
    for i in range(iterr2):
        tim.forward(100)
        tim.right(angle[iterr1])
    iterr1 += 1
    iterr2 += 1
    tim.pencolor(random.choice(colours))

screen = Screen()
screen.exitonclick()
