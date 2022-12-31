from turtle import Turtle

# Constants
FONT_CONFIG = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.hideturtle()
        self.penup()
        self.goto(x=-210, y=250)
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(arg=f"Level: {self.level}", move=False, align="center", font=FONT_CONFIG)

    def increase_level(self):
        self.level += 1
        self.update_level()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER", move=False, align="center", font=FONT_CONFIG)
