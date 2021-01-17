from turtle import Turtle


class MyTurtle(Turtle):
    def __init__(self, posi):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(posi)
        self.setheading(90)

    def move_up(self):
        new_y = self. ycor() + 10
        self.goto(x=self.xcor(), y=new_y)

