# from turtle import Turtle, Screen
#
# wade = Turtle()
#
# print(wade)
# wade.shape("turtle")
# wade.fillcolor("DeepSkyBlue4")
# wade.shapesize(5)
#
# my_screen = Screen()
# my_screen.bgcolor("grey0")
# print(my_screen.canvheight)
# # wade.forward(100)
# my_screen.exitonclick()


from prettytable import PrettyTable, MSWORD_FRIENDLY

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table.align)
# table.set_style(MSWORD_FRIENDLY)
print(table)