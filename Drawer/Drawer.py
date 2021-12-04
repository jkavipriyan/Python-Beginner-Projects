from turtle import Turtle, Screen

arrow = Turtle()


def forward():
    arrow.forward(10)


def backward():
    arrow.backward(10)


def leftward():
    arrow.left(10)


def rightward():
    arrow.right(10)

def clear():
    arrow.clear()
    arrow.penup()
    arrow.home()
    arrow.pendown()


screen = Screen()
screen.listen()
screen.onkey(fun=forward, key='w')
screen.onkey(fun=backward, key='s')
screen.onkey(fun=leftward, key='a')
screen.onkey(fun=rightward, key='d')
screen.onkey(fun=clear, key='c')
screen.exitonclick()
