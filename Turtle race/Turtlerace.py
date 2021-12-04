from turtle import Turtle, Screen
import random

colors = ['red', 'orange', 'purple', 'yellow', 'pink', 'blue']
tim = Turtle(shape='turtle')
tom = Turtle(shape='turtle')
jerry = Turtle(shape='turtle')
jany = Turtle(shape='turtle')
gizzy = Turtle(shape='turtle')
bussy = Turtle(shape='turtle')

turtles = [tim, tom, jerry, jany, gizzy, bussy]
speed = [1,2,3,4,5,6,7,8,9,10]
for color in range(len(colors)):
    for turtle in range(len(turtles)):
        if color == turtle:
            turtles[turtle].color(colors[color])


def move_to_start(object, x_cord, y_cord):
    object.penup()
    object.goto(x=x_cord, y=y_cord)


x_cord = -230
y_cord = -120

screen = Screen()
screen.setup(width=500, height=400)
user_input = screen.textinput(prompt="Choose a colour of turtle you bet upon: ", title='Make a bet')
for turtle in turtles:
    move_to_start(turtle, x_cord, y_cord)
    y_cord += 50
end = False
while not end:
    for turtle in turtles:
        turtle.forward(random.choice(speed))
        if turtle.xcor() >= 220 and turtle.pencolor() == user_input:
            print("You won")
            end = True
        elif turtle.xcor() >= 220:
            print("you lose")
            end = True



screen.exitonclick()
