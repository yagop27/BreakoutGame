from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from bricks import Bricks
from score import Score
from time import sleep

screen = Screen()
screen.bgcolor("blue")
screen.setup(width=800, height=600)
screen.title("Breakout")
screen.tracer(0)

paddle = Paddle()  # Creating the paddle via the class on the paddle file
ball = Ball()  # Creating the ball via the class on the ball file
bricks = []
score = Score()

# Setting up the screen to recognize the keys to move the paddle in game
screen.listen()
screen.onkey(paddle.move_left, "Left")
screen.onkey(paddle.move_right, "Right")

y_cord = 250
for y in range(7):  # Creating the bricks for the game
    y_cord -= 25
    for i in range(16):
        br = Bricks()
        br.goto((-320 + (i * 43), y_cord))
        bricks.append(br)


def reset_bricks():
    y_c = 250
    for line in range(7):
        y_c -= 25
        for x in range(16):
            bricks[x].goto((-320 + (x * 43), y_c))


game_level = 0
game_on = True
while game_on:
    screen.update()
    ball.move()

    if ball.ycor() > 280:  # Detecting collision with the upper wall
        ball.bounce_y()

    if ball.xcor() > 380 or ball.xcor() < -380:  # Detecting collision with the side walls
        ball.bounce_x()

    if 10 < ball.distance(paddle) < 50 and ball.ycor() < -230:  # Detecting collision with the paddle
        ball.bounce_y()

    if ball.ycor() < -280:  # If the ball hit the lower part of the screen it resets the ball and the paddle's position
        sleep(0.5)
        ball.goto((0, -230))
        paddle.goto((0, -250))
        ball.bounce_y()
        sleep(0.5)

    for b in bricks:  # Checking collision with the bricks
        if ball.distance(b) < 30:
            b.goto(1000, 1000)
            ball.bounce_y()
            score.update_score()

    if score.score % 10 == 0:
        speed_increase = score.score / 20
        ball.speed(speed_increase)

    if score.level[game_level] == score.score:
        game_level += 1
        ball.goto((0, -230))
        paddle.goto((0, -250))
        reset_bricks()

screen.exitonclick()
