from turtle import Turtle
import random


class Obstacle(Turtle):

    born_location = [[-200, -200],[-100, 100],[100, 100],[200, -200],[100, -100]]

    def __init__(self, born_location):
        super().__init__()
        self.penup()
        self.speed(0)
        self.color('white')
        self.shape('turtle')
        self.speed = 1
        self.goto(born_location)
        self.setheading(random.randint(0, 360))
        self.position = [self.xcor(), self.ycor()]

    def move(self):
        self.forward(self.speed)
        self.left(0.5)
        if self.xcor() > 270 or self.xcor() < -270:
            self.left(60)
        if self.ycor() > 270 or self.ycor() < -270:
            self.left(60)
        self.position = [self.xcor(), self.ycor()]