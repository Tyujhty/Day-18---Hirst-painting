import turtle

import colorgram
from turtle import Turtle, Screen
import random
screen = Screen()
turtle.colormode(255)
def extract_color(colors, rgb_colors):
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b

        random_color = (r, g, b)
        rgb_colors.append(random_color)
    return rgb_colors

hirst = Turtle()
rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
extract_color(colors, rgb_colors)
y_position = 0

for _ in range(11):
    for _ in range(10):
        hirst.pencolor(random.choice(rgb_colors))
        hirst.dot(20)
        hirst.penup()
        hirst.forward(50)
        hirst.pendown()
    y_position += 50
    hirst.teleport(0,  y_position)






screen.exitonclick()
