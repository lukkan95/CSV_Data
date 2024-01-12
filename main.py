import turtle
from turtle import Screen, shape

import pandas as pd

from scoreboard import Scoreboard
from state_point import StatePoint
from csv_data import StateData
import time


screen = Screen()
image = "blank_states_img.gif"
screen.addshape(image)
shape(image)


scoreboard = Scoreboard()
states = StateData()
states.create_list_from_csv()


guessed_states = []

game_status = True

while game_status:
    screen.update()
    print(guessed_states)
    guess = turtle.textinput("Guess state", "Type a next state or exit to finish:").title()
    if guess == "Exit":

        data_dict = {
            "states": [],
            # "position": []
        }

        for elem in states.list_of_states:
            data_dict["states"].append(elem[0])
            # data_dict["position"].append((elem[1], elem[2]))
        df = pd.DataFrame(data_dict)
        df.to_csv("states_to_learn")

        screen.bye()
    for elem in states.list_of_states:
        if guess in elem and guess not in guessed_states:
            point = StatePoint(elem[0], (int(elem[1]), int(elem[2])))
            scoreboard.add_to_score()
            guessed_states.append(guess)
            states.list_of_states.remove(elem)

screen.exitonclick()




