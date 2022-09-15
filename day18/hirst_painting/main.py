# import colorgram as cg
#
# rgb_color = []
# colors = cg.extract("painting.webp", 2 ** 32)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_color.append(new_color
#                      )
# print(rgb_color)
import random
import turtle as turtle_module

turtle_module.colormode(255)
turtle = turtle_module.Turtle()
turtle.speed("fast")
color_list = [(233, 233, 232), (231, 233, 237), (236, 231, 233), (224, 233, 227), (207, 160, 82), (54, 88, 130), (145, 91, 40), (140, 26, 49), (221, 207, 105), (132, 177, 203), (158, 46, 83), (45, 55, 104), (169, 160, 39), (129, 189, 143), (83, 20, 44), (37, 43, 67), (186, 94, 107), (187, 140, 170), (85, 120, 180), (59, 39, 31), (88, 157, 92), (78, 153, 165), (194, 79, 73), (45, 74, 78), (80, 74, 44), (161, 201, 218), (57, 125, 121), (219, 175, 187), (169, 206, 172), (219, 182, 169), (179, 188, 212), (48, 74, 73), (147, 37, 35), (43, 62, 61)]
number_of_dots = 100
turtle.hideturtle()
turtle.setheading(222)
turtle.penup()

turtle.forward(300)
turtle.setheading(0)

for dot_count in range(1, number_of_dots + 1):
    turtle.dot(20, random.choice(color_list))
    turtle.forward(50)


    if dot_count % 10 == 0:
        turtle.setheading(90)
        turtle.forward(50)
        turtle.setheading(180)
        turtle.forward(500)
        turtle.setheading(0)







screen = turtle_module.Screen()
screen.exitonclick()