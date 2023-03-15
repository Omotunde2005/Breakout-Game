from turtle import Turtle
import random


class Bricks:
    def __init__(self):
        self.colors = ['blue', 'yellow', 'red', 'green', 'orange']
        self.turtles = []
        self.show_bricks()

    def show_bricks(self):
        y_values = [int(y) for y in range(120, 240, 22)]
        x_values = [int(x) for x in range(-250, 350, 61)]
        y_index = 0
        self.loop(x_values, y_values, y_index)

    def loop(self, x_val, y_val, y_index):

        for n in x_val:
            if n == x_val[-1]:
                if y_index < len(y_val) - 1:
                    y_index += 1
                    self.loop(x_val, y_val, y_index)
            else:
                x = n
                y = y_val[y_index]
                brick = Turtle()
                brick.penup()
                brick.shapesize(stretch_len=3)
                brick.color(random.choice(self.colors))
                brick.shape("square")
                brick.goto(x, y)
                self.turtles.append(brick)

