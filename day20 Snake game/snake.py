from turtle import Turtle

starting_positions = [(0, 0), (-20, 0), (-40, 0)]
movement = 20


class Snake:
    def __init__(self):
        self.snakes = []
        self.start_snakes()
        self.head = self.snakes[0]

    def start_snakes(self):
        for position in starting_positions:
            self.add_segment(position)

    def add_segment(self, position):
        snake = Turtle('square')
        snake.color('white')
        snake.penup()
        snake.goto(position)
        self.snakes.append(snake)

    def extend(self):
        self.add_segment(self.snakes[-1].position())

    def move(self):
        for segment in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[segment - 1].xcor()
            new_y = self.snakes[segment - 1].ycor()
            self.snakes[segment].goto(new_x, new_y)
        self.head.forward(movement)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def reset(self):
        for segments in self.snakes:
            segments.goto(1000,1000)
        self.snakes.clear()
        self.start_snakes()
        self.head = self.snakes[0]
