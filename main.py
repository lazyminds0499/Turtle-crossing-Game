from turtle import Screen
from my_turle import MyTurtle
from cars import Car
import time
from score import Score
screen = Screen()
screen.colormode(255)
screen.tracer(0)
score = Score()
tatto = MyTurtle((0, -260))
screen.setup(width=600, height=600)
screen.listen()
screen.onkeypress(fun=tatto.move_up, key="Up")
game_is_on = True
count = 0
cars_list = []
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if count % 6 == 0:
        car = Car()
        cars_list.append(car)
    for cars in range(len(cars_list)):
        cars_list[cars].move()

    for cars in range(len(cars_list) - 1):
        if cars_list[cars].distance(tatto) < 17:
            score.game_over()
            game_is_on = False

    if tatto.ycor() > 260:
        score.game_level()
        tatto.goto(0, -260)
        for car in cars_list:
            car.speed += 2

    count += 1
screen.exitonclick()
