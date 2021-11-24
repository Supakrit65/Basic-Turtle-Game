from turtle import Turtle
import math


class Player(Turtle):
    def __init__(self, name, color):
        super().__init__()
        self.penup()
        self.shape('turtle')
        self.color(color)
        self.speed = 2
        self.name = name
        self.position = [0, 0]
        self.score = 0
        self.is_alive = True
        self.color = color

    def move(self):
        self.forward(self.speed)
        # Border Checking
        if self.xcor() > 270 or self.xcor() < -270:
            self.left(60)
        if self.ycor() > 270 or self.ycor() < -270:
            self.left(60)
        # update position attribute
        self.position = [self.xcor(), self.ycor()]

    def turn_left(self):
        self.left(30)

    def turn_right(self):
        self.right(30)

    def is_collision_item(self, _item):
        a = self.xcor() - _item.xcor()
        b = self.ycor() - _item.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2))
        if distance < 20:
            return True
        else:
            return False

    def is_collision_obs(self, obstacle):
        a = self.xcor() - obstacle.xcor()
        b = self.ycor() - obstacle.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2))
        if distance < 20:
            return True
        else:
            return False
