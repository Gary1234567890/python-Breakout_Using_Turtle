from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.start_speed = 0.6
        self.color("white")
        self.shape("circle")
        self.penup()
        self.goto(0, -200)
        self.x_direction = self.start_speed
        self.y_direction = self.start_speed
        self.hit_count = 0

    def move(self):
        if self.xcor() >= 490 or self.xcor() <= -490:
            self.x_direction *= -1

        if self.ycor() >= 380:
            self.y_direction *= -1

        new_x = self.xcor() + self.x_direction
        new_y = self.ycor() + self.y_direction
        self.goto(new_x, new_y)

    def bounce_off_surface(self):
        self.y_direction *= -1
        self.hit_count += 1
        #self.x_direction *= 1.03
        self.y_direction *= 1.03

    def bounce_off_paddle(self, ball_x, paddle_x):
        self.x_direction = (ball_x - paddle_x) * 0.025
        self.y_direction *= -1
        self.hit_count += 1
        #self.x_direction *= 1.03
        self.y_direction *= 1.03

    def reset(self):
        self.hit_count = 0
        self.goto(0, 0)
        self.x_direction = self.start_speed
        self.y_direction = self.start_speed
