import random
from turtle import Screen
import turtle as t

pen = t.Turtle()
# pen.shape("turtle")

# for _ in range(10):
#     pen.forward(10)
#     pen.penup()
#     pen.forward(10)
#     pen.pendown()
#

#
#
# def draw_shape(numsides):
#     angle = 360/numsides
#     for _ in range(numsides):
#         pen.forward(100)
#         pen.right(angle)
#
# for shape_side_n in range(3,11):
#     pen.color(random.choice(colours))
#     draw_shape(shape_side_n)

# for _ in range(3):
#     pen.color("cyan")
#     pen.forward(100)
#     pen.right(120)
#
# for _ in range(4):
#     pen.color("green")
#     pen.forward(100)
#     pen.right(90)
#
# for _ in range(5):
#     pen.color("blue")
#     pen.forward(100)
#     pen.right(72)
#
# for _ in range(6):
#     pen.color("pink")
#     pen.forward(100)
#     pen.right(60)
#
# for _ in range(7):
#     pen.color("#FBF2CF")
#     pen.forward(100)
#     pen.right(51)
#
# for _ in range(8):
#     pen.color("#FA7070")
#     pen.forward(100)
#     pen.right(45)
#
# for _ in range(9):
#     pen.color("#C6EBC5")
#     pen.forward(100)
#     pen.right(40)
#
# for _ in range(10):
#     pen.color("#A1C298")
#     pen.forward(100)
#     pen.right(36)



t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    rgb = (r,g,b)
    return rgb

# directions = [0, 90, 180, 270]
# pen.pensize(15)
# pen.speed("fast")
#
# for _ in range(200):
#     pen.color(random_color())
#     pen.forward(30)
#     pen.setheading(random.choice(directions))




pen.speed("fastest")



def draw_spirograph(space):
    for _ in range(int(360/space)):
        current_heading = pen.heading()
        pen.color(random_color())
        pen.circle(100)
        pen.setheading(current_heading + 5)

draw_spirograph(5)


screen = Screen()
screen.exitonclick()