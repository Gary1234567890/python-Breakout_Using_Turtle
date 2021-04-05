from turtle import Screen
from paddle import Paddle
from ball import Ball
from block import Block

screen = Screen()
screen.setup(width=1000, height=768)
screen.bgcolor("black")
screen.title("Breakout")
screen.tracer(n=2, delay=0)

paddle = Paddle(0, -300)
ball = Ball()

screen.listen()
screen.onkey(paddle.go_left, "Left")
screen.onkey(paddle.go_right, "Right")

row_of_blocks = []
for i in range(20):
    block = Block(-475 + (i * 50), 300, "red")
    row_of_blocks.append(block)

game_is_on = True

while game_is_on:
    screen.update()
    ball.move()

    #Detect collision with paddles
    if ball.distance(paddle) < 50 and ball.ycor() < -280:
        ball.bounce_off_paddle(ball.xcor(), paddle.xcor())

    #Detect collision with blocks
    for block in row_of_blocks:
        if ball.distance(block) < 25 and 285 < ball.ycor() < 315:
            ball.bounce_off_surface()
            row_of_blocks.remove(block)
            block.reset()

    #Reset ball
    if ball.ycor() < -380:
        ball.reset()

screen.exitonclick()
