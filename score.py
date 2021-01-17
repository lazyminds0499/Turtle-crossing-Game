from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.hideturtle()
        self. goto(-280, 260)
        self.game_level()

    def game_level(self):
        self.clear()
        self.write(arg=f"Level: {self.level}", align="left", font=("courier", 15, "normal"))
        self.level += 1

    def game_over(self):
        self.goto(-20, 0)
        self.write(arg="Game over", align="left", font=("courier", 15, "bold"))
