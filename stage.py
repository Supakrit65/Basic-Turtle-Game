from turtle import Turtle, Screen
import json
from obstacle import Obstacle
from item import Item
from score import Score
from border import Border


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
        self.screen.tracer(5)
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

    def add_obs(self, n):
        born_location = [[-200, -200], [-100, 100], [100, 100], [-150, 250],
                         [100, -150], [150, 200], [0, -180], [80,-80]]
        for i in range(n):
            self.obstacles.append(Obstacle(born_location[i]))

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
        text.write(f'Game over: \n\nYour score is {score.score}', font=style, align='center')
        text.goto(120, -270)
        end_style = ('Arial', 12)
        text.write('click the screen to exit', font=end_style)
        self.screen.exitonclick()
