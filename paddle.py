from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=0.75, stretch_len=6)
        self.goto((0, -250))
        self.speed('fast')

    def move_left(self):
        if self.xcor() > -350:
            new_x = self.xcor() - 50
            self.goto(new_x, self.ycor())

    def move_right(self):
        if self.xcor() < 350:
            new_x = self.xcor() + 50
            self.goto(new_x, self.ycor())
