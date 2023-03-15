from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super(Ball, self).__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.x = 10
        self.y = 10
        self.move_speed = 0.1

    def move(self):
        x = self.xcor() + self.x
        y = self.ycor() + self.y
        self.goto(x, y)

    def bounce_x(self):
        self.x *= -1

    def bounce_y(self):
        self.y *= -1

    def restart(self):
        self.goto(x=-235, y=0)

