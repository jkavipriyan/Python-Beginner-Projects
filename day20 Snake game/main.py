from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()
screen.listen()

screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    score.display_score()
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend()
    if snake.head.xcor() > 282 or snake.head.xcor() < -282 or snake.head.ycor() > 300 or snake.head.ycor() < -285:
        snake.reset()
        score.reset()

    for segments in snake.snakes[1:]:
        if snake.head.distance(segments) < 10:
            snake.reset()
            score.reset()

screen.exitonclick()
