from turtle import Turtle
import random


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.r = random.randint(0, 255)
        self.g = random.randint(0, 255)
        self.b = random.randint(0, 255)
        self.colors = (self.r, self.g, self.b)
        self.new_y = random.randint(-240, 240)
        self.new_x = random.randint(290, 400)
        self.car = random.randint(4, 12)
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=0.8, stretch_len=2)
        self.color(self.colors)
        self.speed = 5

    def move(self):
        self.setheading(180)
        self.new_x -= self.speed
        self.goto(x=self.new_x, y=self.new_y)