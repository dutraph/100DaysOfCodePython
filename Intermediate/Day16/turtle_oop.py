# from turtle import Turtle, Screen
#
# timmy = Turtle()
# my_screen = Screen()
#
# timmy.shape("turtle")
# timmy.color("coral")
# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90)
#
#
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ['Pikachu', 'Squirtle', 'Charmander', 'Bulbasaur'])
table.add_column("Type", ['Electric', 'Water', 'Fire', 'Plant'])

table.align = 'l'
print(table)
