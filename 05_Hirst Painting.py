# import colorgram
import turtle
import random

### using colorgram to extract colors from an image

# colors = colorgram.extract('image.jpeg', 30)
# rgb_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

### copy generated colors into a list and remove colors close to white

colors_list = [(200, 172, 112), (155, 180, 195), (153, 185, 174), (193, 162, 177), (214, 204, 117),
               (208, 180, 195), (176, 188, 212), (162, 211, 187), (164, 202, 213), (115, 122, 183),
               (188, 170, 60), (212, 182, 180), (199, 206, 45)]

### start Turtle()

timmy = turtle.Turtle()
turtle.colormode(255)
turtle.speed("fastest")

turtle.teleport(-200,-200)
turtle.hideturtle()

for _ in range (10):

    for _ in range (10):
        turtle.dot(20, random.choice(colors_list))
        turtle.penup()
        turtle.forward(50)
        turtle.pendown()

    turtle.penup()
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(500)
    turtle.left(180)


turtle.Screen()
turtle.exitonclick()