# import turtle
#
# import model
# print(f"Var{model.another_var}")
#
# from turtle import Turtle, Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("#FF7F50")
# timmy.forward(100)
# my_screen = Screen()
# print(my_screen.canvheight)
#
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "squirtle", "Charmander"])
table.add_column("Type ", ["Electric", "Water", "Fire"])

align = "l"

table.align = align

print(table)


