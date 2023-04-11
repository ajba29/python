#turtle graphics demo
import turtle
from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("blue")
timmy.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

#pretty table demo
import prettytable

from prettytable import PrettyTable



table = PrettyTable()

table.add_column("Pokemon Name",["Pikachu","Bulbasaur","Charmander","Squirtle"])
table.add_column("Type",["Electric","Grass","Fire","Water"])
table.align = "l"

print(table)