from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 10, 'normal')


class StatePoint(Turtle):

    def __init__(self, name_of_state, position):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("red")
        self.goto(position)
        self.write(f"{name_of_state}", align=ALIGNMENT, font=FONT)
