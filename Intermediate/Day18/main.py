from turtle import *
import turtle

tur = turtle.Turtle()
# for i in range(15):
#     tur.forward(10)
#     tur.penup()
#     tur.forward(10)
#     tur.pendown()

colours = ['black', 'red', 'green', 'yellow', 'blue', 'orange', 'pink', 'purple', 'cyan']
tur.setpos(0.0, 0.0)


def geometry_rigth(sides, colour):
    for _ in range(sides):
        tur.color(colour)
        tur.forward(100)
        tur.right(360/sides)


def geometry_left(sides, colour):
    for _ in range(sides):
        tur.color(colour)
        tur.forward(100)
        tur.left(360/sides)


count = 3
while count <= 10:
    colour = colours[count-3]
    geometry_rigth(count, colour)
    count += 1
    if count == 11:
        count = 3
        while count <= 10:
            colour = colours[count - 3]
            geometry_left(count, colour)
            count += 1


screen = Screen()
screen.exitonclick()