from turtle import Turtle, Screen
import json
from obstacle import Obstacle
from item import Item
from score import Score
from border import Border
import random
from player import Player
import math


class Stage(Turtle):
    def __init__(self, border, screen):
        """Initialize a stage with the border."""
        super().__init__()
        self.border = border
        self.screen = screen
        self.items = []
        self.obstacles = []

    def create_screen(self, player):
        # create GUI screen
        Stage.show_title()
        self.screen.bgcolor('#F0CBCC')
        self.screen.title('Simple Turtle GUI Game by Supakrit')
        self.screen.setup(width=660, height=660)
        self.screen.bgpic('sWallper.gif')
        self.screen.register_shape('foodpic.gif')
        # update screen manually
        self.screen.tracer(0)
        # create border
        self.border.draw_border()
        self.screen.listen()
        self.screen.onkey(fun=player.turn_left, key='Left')
        self.screen.onkey(fun=player.turn_right, key='Right')

    def ask_input(self):
        user_name = self.screen.textinput(title='Make your decision', prompt='Username of player: ')
        user_color = self.screen.textinput(title='Make your decision',
                                           prompt='Pick your player\'s color (blue, yellow, green) : ').lower()
        while user_color not in ['yellow', 'blue', 'green']:
            print('Please choose valid color choice.')
            user_color = self.screen.textinput(title='Make your decision', prompt='Pick your player\'s color (blue, '
                                                                                  'yellow, green) : ').lower()
        return user_name, user_color

    def update_screen(self):
        self.screen.update()

    def add_item(self, n):
        for i in range(n):
            self.items.append(Item())

    def add_obs(self, n, player, late):
        born_location_list = [[-200, -200], [-100, 100], [220, 100], [-150, 250],
                         [100, -150], [150, 200], [0, -180]]
        for i in range(n):
            born_location = [random.randint(-270, 270), random.randint(-270, 270)]
            if late:
                while True:
                    a = player.xcor() - born_location[0]
                    b = player.ycor() - born_location[1]
                    distance = math.sqrt((a ** 2) + (b ** 2))
                    if distance < 60 or distance > 160:
                        born_location = [random.randint(-270, 270), random.randint(-270, 270)]
                    else:
                        break
                self.obstacles.append(Obstacle(born_location))
            else:
                self.obstacles.append(Obstacle(random.choice(born_location_list)))

    @staticmethod
    def show_title():
        title = Turtle()
        title.penup()
        title.hideturtle()
        title.speed(0)
        title.color('#203EE7')
        title.goto(-85,293)
        title.write(f'Feast of the Turtle', False,
                    font=("Verdana", 15, 'bold'))

    def end(self, score):
        text = Turtle()
        self.screen.clear()
        Stage.show_title()
        self.screen.bgcolor('#F0CBCC')
        self.screen.title('Simple Turtle GUI Game by Supakrit')
        self.screen.setup(width=660, height=660)
        self.screen.bgpic('sWallper.gif')
        score.show_high_score()
        text.penup()
        text.hideturtle()
        text.color('#8CF310')
        text.goto(0, 0)
        style = ('Courier', 30, 'italic')
        if score.score > score.old_high_score:
            text.goto(0, -50)
            text.write(f'Game over:\nYou got a HIGH SCORE!\n\n'
                       f'Your score is {score.score}', font=style, align='center')
        else:
            text.write(f'Game over:\n\n'
                       f'Your score is {score.score}', font=style, align='center')
        text.goto(120, -270)
        end_style = ('Arial', 12)
        text.write('click the screen to exit', font=end_style)

        self.screen.exitonclick()
