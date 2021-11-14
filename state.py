from turtle import Turtle


class State(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

    def go_to(self, x, y, enter_state):
        self.goto(x, y)
        self.write(f"{enter_state}", align="center")