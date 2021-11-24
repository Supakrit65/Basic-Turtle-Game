from turtle import Turtle


class Border(Turtle):
    def __init__(self, corner, width, height):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.color('white')
        self.pensize(5)
        self.corner = corner
        self.height = height
        self.width = width

    def draw_border(self):
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.color('white')
        self.pensize(5)
        self.penup()
        self.goto(self.corner[0], self.corner[1])
        self.pendown()
        self.goto(self.corner[0], self.height)
        self.goto(self.width, self.height)
        self.goto(self.width, self.corner[1])
        self.goto(self.corner[0], self.corner[1])