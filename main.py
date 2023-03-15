import time
from turtle import Turtle, Screen
from paddle import Paddle
from bricks import Bricks
from ball import Ball
from lives import Lives

screen = Screen()
screen.title("Breakout Game")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.listen()

screen.tracer(0)
pad = Paddle()
brick = Bricks()
ball = Ball()
live = Lives()
screen.onkey(key="Right", fun=pad.move_right)
screen.onkey(key="Left", fun=pad.move_left)


while True:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if len(live.trials) == 0:
        live.game_over()
        with open("records.txt", mode="r") as data:
            lines = data.readlines()
        if live.score > int(lines[0]):

            with open("records.txt", mode="w") as file:
                file.write(f"{live.score}")
        break
    if ball.xcor() > 260 or ball.xcor() < -270:
        ball.bounce_x()

    if ball.distance(pad) < 36:
        ball.bounce_y()

    if ball.ycor() > 240:
        ball.bounce_y()

    if ball.ycor() < -265:
        live.check_trials()
        ball.restart()
        time.sleep(0.5)

    for block in brick.turtles:
        if ball.distance(block) < 30:
            live.check_score()
            block.hideturtle()
            brick.turtles.remove(block)
            ball.bounce_y()

    if len(brick.turtles) < 50:
        ball.move_speed = 0.03


screen.exitonclick()
