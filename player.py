from turtle import Turtle

# Constants
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.setheading(90)
        self.penup()
        self.goto(x=STARTING_POSITION[0], y=STARTING_POSITION[1])

    def move(self):
        self.forward(MOVE_DISTANCE)

    def finished_round(self):
        if self.ycor() > FINISH_LINE_Y:
            self.goto(x=STARTING_POSITION[0], y=STARTING_POSITION[1])
            return True
