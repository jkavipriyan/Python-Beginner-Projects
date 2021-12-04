import random
from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Scoreboard
import time

screen = Screen()

screen.setup(height=800, width=1000)
screen.bgcolor('black')
screen.tracer(0)

paddle1 = Paddle(-480)
paddle2 = Paddle(475)
score1 = Scoreboard(250)
score2 = Scoreboard(-250)
bal = Ball()
screen.listen()
screen.onkeypress(paddle1.paddle_up, 'w')
screen.onkeypress(paddle1.paddle_down, 's')
screen.onkeypress(paddle2.paddle_up, 'Up')
screen.onkeypress(paddle2.paddle_down, 'Down')
end_game = False
bal.ball.setheading(random.choice(range(0,360)))

while not end_game:
    screen.update()
    time.sleep(0.1)
    if 490 > bal.ball.xcor() > -490 and 380 > bal.ball.ycor() > -380:
        bal.move_ball()
    if not 380 >= bal.ball.ycor() > -380:
        bal.set_heading()
        bal.move_ball()
    if 490 <= bal.ball.xcor():
        score2.increase_score()
        score2.write_score()
        bal.ball.home()
    if -490 >= bal.ball.xcor():
        score1.increase_score()
        score1.write_score()
        bal.ball.home()
    for segments in paddle1.segment:
        if bal.ball.distance(segments) < 15:
            bal.reflect()
            bal.move_ball()
    for segments in paddle2.segment:
        if bal.ball.distance(segments) < 15:
            bal.reflect()
            bal.move_ball()

screen.exitonclick()
