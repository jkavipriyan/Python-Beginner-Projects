from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_cord):
        super().__init__()
        self.y_cord = 0
        self.segment = []
        self.x = x_cord
        self.add_segment(self.x)
        self.y_cord = 0


    def add_segment(self, x_cord):
        for _ in range(4):
            self.segments(x_cord)

    def segments(self, x_cord):
        paddle = Turtle()
        paddle.color('white')
        paddle.shape('square')
        paddle.penup()
        paddle.setheading(90)
        paddle.goto(x=x_cord, y=self.y_cord)
        self.y_cord += 20
        self.segment.append(paddle)

    def paddle_up(self):
        for segments in range(len(self.segment) - 1, -1, -1):
            self.segment[segments].goto(self.x, self.segment[segments].ycor() + 20)

    def paddle_down(self):
        for segments in range(len(self.segment) - 1, -1, -1):
            self.segment[segments].goto(self.x, self.segment[segments].ycor() - 20)
