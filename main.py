import colorgram
from turtle import Turtle, Screen
import random
screen = Screen()
def extract_color(colors, rgb_colors):
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b

        random_color = (r, g, b)
        rgb_colors.append(random_color)
    print(rgb_colors)
    return rgb_colors

hirst = Turtle()
rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
extract_color(colors, rgb_colors)

for _ in range(10):
    hirst.dot(10)
    hirst.forward(10)






screen.exitonclick()
