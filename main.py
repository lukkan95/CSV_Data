import turtle
from turtle import Screen, shape
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

# screen.onkey(screen.bye, "Escape")
# screen.listen()

guessed_states = []

game_status = True

while game_status:
    screen.update()
    guess = turtle.textinput("Guess state", "Type a next state or exit to finish:")
    if guess == "exit":
        screen.bye()
    for elem in states.list_of_states:
        if guess in elem and guess not in guessed_states:
            point = StatePoint(elem[0], (int(elem[1]), int(elem[2])))
            scoreboard.add_to_score()
            guessed_states.append(guess)

screen.exitonclick()




