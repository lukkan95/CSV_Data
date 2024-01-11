from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 32, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.current_score = 0
        self.hideturtle()
        self.penup()
        self.goto(400, -400)
        self.write(f"{self.current_score}/50", font=FONT, align=ALIGNMENT)

    def add_to_score(self):
        self.current_score += 1
        self.clear()
        self.write(f"{self.current_score}/50", font=FONT, align=ALIGNMENT)


