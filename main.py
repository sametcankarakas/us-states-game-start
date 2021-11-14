import turtle
from state import State

import numpy as np
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
counter = 0
game_is_on = True
counter_str = "Guess the state"

data = pandas.read_csv("50_states.csv")
state_list = data.state.to_list()

while game_is_on:
    answer_state = screen.textinput(title=f"{counter_str}", prompt="What's another state's name?")
    if answer_state in state_list:
        chosen_state = data[data["state"] == f"{answer_state}"]
        counter += 1
        x = int(chosen_state["x"])
        y = int(chosen_state["y"])
        fck = State()
        fck.go_to(x=x, y=y, enter_state=answer_state)
        counter_str = str(counter) + "/50 States Correct"
        state_list.remove(f"{answer_state}")
        print(state_list)
        if counter == 50:
            game_is_on = False

    # for state in state_list:

    # chosen_state = data[data["state"] == f"{answer_state}"]
    # state = chosen_state.iloc[0, 0]
    # print(state)
    # print(type(state))
    # if answer_state == state:
    #     counter += 1
    # x = int(chosen_state["x"])
    # y = int(chosen_state["y"])
    # fck = State()
    # fck.go_to(x=x, y=y, enter_state=answer_state)
    # counter_str = str(counter) + "/50 States Correct"

        # state_turtle = turtle.Turtle()
        # state_turtle.hideturtle()
        # state_turtle.penup()
        # state_turtle.goto(x, y)
        # state_turtle.write(f"{answer_state}", align="center")



screen.exitonclick()
