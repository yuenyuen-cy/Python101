from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color: ")
colors = [
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "purple",
]

y_position = [-125, -75, -25, 25, 75, 125]
all_turtles = []

for turtle_index in range (0, 6):
    new_turtle = Turtle(shape ="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x = -200, y = y_position[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} is the winner!")
            else:
                print(f"You lost :( The {winning_color} is the winner.")

        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)

screen.exitonclick()