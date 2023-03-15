from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=0.5, stretch_len=5)
        self.penup()
        self.color("white")
        self.goto(x=0, y=-250)

    def move_right(self):
        new_x = self.xcor() + 20
        self.goto(x=new_x, y=self.ycor())

    def move_left(self):
        new_x = self.xcor() - 20
        self.goto(x=new_x, y=self.ycor())
