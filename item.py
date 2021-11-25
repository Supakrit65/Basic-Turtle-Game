from turtle import Turtle
import random


class Item(Turtle):
    """
    Maintain Item objects which move randomly.
    Item class is a subclass of Turtle class.
    Initialize with properties.
    """
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed(0)
        self.color('#AFE0EE')
        self.shape('item.gif')
        self.speed = 0.5
        self.goto(x=random.randint(-270, 270), y=random.randint(-270, 270))
        self.setheading(random.randint(0, 360))
        self.position = [self.xcor(), self.ycor()]

    def jump(self):
        self.goto(x=random.randint(-270, 270), y=random.randint(-270, 270))
        self.setheading(random.randint(0, 360))
        self.position = [self.xcor(), self.ycor()]

    def move(self):
        self.forward(self.speed)
        # Border Checking
        if self.xcor() > 270 or self.xcor() < -270:
            self.left(60)
        if self.ycor() > 270 or self.ycor() < -270:
            self.left(60)
        self.position = [self.xcor(), self.ycor()]

