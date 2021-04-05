from turtle import Turtle


class Block(Turtle):
    def __init__(self, x, y, color):
        super().__init__()
        self.turtlesize(stretch_wid=1, stretch_len=2.4, outline=1)
        self.shape("square")
        self.color(color)
        self.penup()
        self.goto(x, y)
        self.hit_count = 0
