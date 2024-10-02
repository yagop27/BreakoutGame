from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from bricks import Bricks

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Breakout")

paddle = Paddle()  # Creating the paddle via the class on the paddle file
ball = Ball()  # Creating the ball via the class on the ball file

# Setting up the screen to recognize the keys to move the paddle in game
screen.listen()
screen.onkey(paddle.move_left, "Left")
screen.onkey(paddle.move_right, "Right")
y_cord = 295
for y in range(7):
    y_cord -= 25
    for i in range(16):
        Bricks((-320 + (i * 43), y_cord))

game_on = True
while game_on:
    screen.update()
    ball.move()

    if ball.ycor() > 280:  # Detecting collision with the upper wall
        ball.bounce_y()

    if ball.xcor() > 380 or ball.xcor() < -380:  # Detecting collision with the side walls
        ball.bounce_x()

    if ball.distance(paddle) < 50 and ball.ycor() < -230:
        ball.bounce_y()

    if ball.ycor() < -260:
        print('You lose')
        break

screen.exitonclick()
