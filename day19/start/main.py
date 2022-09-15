from turtle import Turtle, Screen


turtle = Turtle()
screen = Screen()


def move_forwards():
    turtle.forward(10)


def turn_right():
    new_heading = turtle.heading() - 10
    turtle.setheading(new_heading)


def turn_left():
    new_heading = turtle.heading() + 10
    turtle.setheading(new_heading)


def move_backward():
    turtle.backward(10)

def clear():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()

screen.listen()
screen.onkey(key="Left", fun=turn_left)
screen.onkey(key="Up", fun=move_forwards)
screen.onkey(key="Down", fun=move_backward)
screen.onkey(key="Right", fun=turn_right)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
