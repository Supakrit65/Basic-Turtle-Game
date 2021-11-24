from turtle import Turtle, Screen
import json
from obstacle import Obstacle
from item import Item
from player import Player
from score import Score
from border import Border
from stage import Stage
import time


def app_mode():
    interface = Screen()
    interface.register_shape('interface_wallpaper.gif')
    # show my project name and my name
    project_name = Turtle()
    interface.setup(width=400, height=400)
    interface.bgpic('interface_wallpaper.gif')
    interface.title('Basic Turtle Game')
    project_name.hideturtle()
    project_name.color('#8BF412')
    style = ('Courier', 15, 'italic')
    project_name.write(f'Welcome to my Turtle Game:\n<please set your mode>', font=style, align='center')
    project_name.penup()
    project_name.goto(150, -150)
    project_name.color('#E5FB07')
    project_name.write(f'Thank you\n<Supakrit65>', font=style, align='right')
    # Pop up a dialog window for input of app mode
    mode_choice = interface.textinput('App Mode', 'Type (p) to play a game or '
                                                  '(v) to view your score or (q) to quit: ').lower()
    # if input is invalid ask of input again
    while mode_choice not in ['p', 'v', 'q']:
        # show a warning message on the screen for invalid input
        warning = Turtle()
        warning.hideturtle()
        warning.penup()
        warning.goto(-150, -80)
        warning.color('white')
        warning.write('Warning:\nPlease give a valid input', font=("Arial", 10, "normal"))
        mode_choice = interface.textinput('App Mode', 'Type (p) to play a game or '
                                                      '(v) to view your score or (q) to quit: ').lower()
        warning.clear()
    if mode_choice == 'p':
        project_name.clear()
        game_mode()

    elif mode_choice == 'v':
        view_mode(interface, project_name)
    else:
        print('App Closed')


def game_mode():
    stage_corner = [-280, -280]
    stage_height = 280
    stage_width = 280
    # create a stage and border
    border = Border(stage_corner, stage_height, stage_width)
    stage = Stage(border, Screen())
    # pop up dialog window for user input
    user_name, user_color = stage.ask_input()
    player = Player(user_name, user_color)
    stage.create_screen(player)
    stage.add_item(10)
    stage.add_obs(4, player, False)
    score = Score()
    high_score = Score()
    # show install score which is 0
    score.update_score(player)
    high_score.show_high_score()
    delay_obs = 200   # delay loop for obstacle spawn
    delay_item = 300  # delay loop for obstacle spawn
    delay_count_obs = 0
    delay_count_item = 0
    time_sleep = 0.0001
    # start game loop
    while True:
        stage.update_screen()
        player.move()
        for item in stage.items:
            item.move()
            if player.is_collision_item(item):
                item.jump()
                score.change_score(100, player)
        if delay_count_obs == delay_obs:
            stage.add_obs(1, player, True)
            delay_count_obs = 0
            delay_obs *= 2
        if delay_count_item == delay_item:
            stage.add_item(1)
            delay_count_item = 0
        for obs in stage.obstacles:
            obs.move()
            if player.is_collision_item(obs):
                score.old_high_score = score.get_high_score()
                score.save_score(player)
                stage.end(score)
        delay_count_obs += 1
        delay_count_item += 1
        # relay the screen update
        time.sleep(time_sleep)


def view_mode(screen, user_data):
    screen.clearscreen()
    screen.setup(400, 400)
    instruction = Turtle()
    instruction.hideturtle()
    style = ('Courier', 15, 'italic')
    instruction.write('Please type your username\nyou what to view score', font=style, align='center')
    screen.bgcolor('#D8FA04')
    username = screen.textinput('View Mode', 'Please type your username you what to view score: ')
    instruction.clear()
    message = view_score(username)
    user_data.penup()
    user_data.goto(0, -50)
    user_data.pendown()
    user_data.color('black')
    user_data.write(f'Username: {username}\n{message}\n\n\nclick to exit the window',
                    font=("Calibri", 18, "bold"), align='center')
    screen.exitonclick()


def view_score(username):
    try:
        with open('game_data.json', 'r') as data_file:
            data_dict = json.load(data_file)
    except FileNotFoundError:
        return f'No Data File Found'
    else:
        if username in data_dict:
            color = data_dict[username]['color']
            your_score = data_dict[username]['score']
            return f'Color: {color}\nScore: {your_score}'
        else:
            return f'No details for {username} exists.'


# Main
app_mode()