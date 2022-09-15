import random
import turtle
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500,height=400)
is_race_on = False
user_bet = screen.textinput(title="Make Your Bet",prompt="Which Turtle will win the race? Enter a Color: ")
color = ["violet","indigo","blue","green","orange","red","black"]
y_positions = [80,-70,50,-40,-10,20,-100]
all_turtles = []

for turtle_index in range(0, 7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-220, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 220:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print("You've won!")
            else:
                print(f"You've Lost! The {winning_color} turtle is the winner!")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)





screen.exitonclick()