import time
from turtle import Screen
from paddle import Paddle
from bricks import Bricks
from ball import Ball
from scores import ScoreBoard

screen = Screen()
screen.title("Breakout Game")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.listen()

screen.tracer(0)
pad = Paddle()
brick = Bricks()
ball = Ball()
lives = ScoreBoard()
screen.onkey(key="Right", fun=pad.move_right)
screen.onkey(key="Left", fun=pad.move_left)


while True:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if len(lives.trials) == 0:
        lives.game_over()
        with open("records.txt", mode="r") as data:
            lines = data.readlines()
        if lives.score > int(lines[0]):

            with open("records.txt", mode="w") as file:
                file.write(f"{lives.score}")
        break
    if ball.xcor() > 260 or ball.xcor() < -270:
        ball.bounce_x()

    if ball.distance(pad) < 30:
        ball.bounce_y()

    if ball.ycor() > 240:
        ball.bounce_y()

    if ball.ycor() < -260:
        lives.check_trials()
        ball.restart()
        time.sleep(0.5)

    for block in brick.bricks:
        if ball.distance(block) < 30:
            lives.check_score()
            block.hideturtle()
            brick.bricks.remove(block)
            ball.bounce_y()

    if len(brick.bricks) < 50:
        ball.move_speed = 0.05


screen.exitonclick()
