import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

answer_state = screen.textinput(title = "Guess the State", prompt = "Name a state to start." ).title()

data = pd.read_csv("50_states.csv")
state_names = data.state.to_list()

game_is_on = True
guessed_states = []

while len(guessed_states) < 50:

    if answer_state == "Exit":
        missing_states = []
        for state in state_names:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in state_names:
        guessed_states.append(answer_state)
        state_data = data[data.state == answer_state]
        text = turtle.Turtle()
        text.penup()
        text.hideturtle()
        text.color("black")
        text.goto(state_data.x.item(), state_data.y.item())
        text.write(answer_state)
        answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Guessed",
                                        prompt="Good job! What's another state?").title()

    else:
        answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Guessed",
                                        prompt="Wrong, guess again.").title()