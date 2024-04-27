from turtle import Turtle
import random


class Bricks:
    def __init__(self):
        self.colors = ['blue', 'yellow', 'red', 'green', 'orange']
        self.bricks = []
        self.show_bricks()

    def show_bricks(self):
        y_values = [int(y) for y in range(120, 240, 22)]
        x_values = [int(x) for x in range(-250, 350, 61)]
        y_index = 0
        self.loop(x_values, y_values, y_index)

    def loop(self, x_values, y_values, y_index):

        for n in x_values:
            # Check if it is the last position in the x_values list.
            if n == x_values[-1]:

                # Check if all the positions in the y_values has been occupied
                if y_index < len(y_values) - 1:
                    y_index += 1

                    # Run the method again if there are still vacant positions.
                    self.loop(x_values, y_values, y_index)

            # Create new bricks
            else:
                x = n
                y = y_values[y_index]
                brick = Turtle()
                brick.penup()
                brick.shapesize(stretch_len=3)
                brick.color(random.choice(self.colors))
                brick.shape("square")
                brick.goto(x, y)
                self.bricks.append(brick)

