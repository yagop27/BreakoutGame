from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto((350, 230))
        self.score = 0
        self.write(self.score, align="center", font=("Courier", 50, "normal"))
        self.level = [112, 224, 336]

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(self.score, align="center", font=("Courier", 50, "normal"))
