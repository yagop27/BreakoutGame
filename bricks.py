from turtle import Turtle


class Bricks(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_len=2, stretch_wid=0.7)
        self.speed('fastest')

