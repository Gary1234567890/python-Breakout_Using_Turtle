from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.turtlesize(stretch_wid=1, stretch_len=4.8, outline=1)
        self.penup()
        self.goto(x, y)

    def go_right(self):
        new_x = self.xcor() + 50
        self.goto(new_x, self.ycor())

    def go_left(self):
        new_x = self.xcor() - 50
        self.goto(new_x, self.ycor())
