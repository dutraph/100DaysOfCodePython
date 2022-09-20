from turtle import *
from random import choice, uniform

"""
colours = ["CornflowerBlue", "DarkOrchid", 
           "IndianRed", "DeepSkyBlue", "LightSeaGreen", 
           "wheat", "SlateGray", "SeaGreen"]
"""

tur = Turtle()

red = round(uniform(0.00, 256.00), 1)
green = round(uniform(0.00, 256.00), 1)
blue = round(uniform(0.00, 256.00), 1)

tup = (red, green, blue)

directions = [0, 90, 180, 270]


for _ in range(300):
    tur.speed(0)
    tur.pensize(15)
    tur.pencolor(tup)
    tur.forward(30)
    tur.setheading(choice(directions))

screen = Screen()
screen.exitonclick()
