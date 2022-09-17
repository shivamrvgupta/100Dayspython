import time
from turtle import Turtle, Screen
from snake import Snake
from food import  Food
from score import  Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Nokia Snake Game")
screen.tracer(0)

score = Scoreboard()
snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect The Food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.snake_extend()
        score.increase_score()

    # Detect Colloision
    if snake.head.xcor() > 285 or  snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        game_is_on = False
        score.game_over()

    #Detect Colloision with head
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()
















screen.exitonclick()