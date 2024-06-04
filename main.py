
import turtle
from turtle import Turtle, Screen
import random


timmy = Turtle()

# Creating a random walk with random colors using tuples
turtle.colormode(255)  # in order to use r, g, b values to generate any random colour
                   # we need to set colormode in turtle module to 255(largest rgb value)
timmy.speed("fastest")
def random_colour():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb_tuple = (r, g, b)          # Tuple is a datatype which is same like list
                                  # but it is immutable i.e we cannot change values
                                  # that it has
    return rgb_tuple

directions = [0, 90, 180, 270]
for _ in range(200):
    timmy.pencolor(random_colour())
    timmy.left(random.choice(directions))
    timmy.forward(20)

screen = Screen()
screen.exitonclick()