from turtle import Turtle, Screen
import json
from obstacle import Obstacle
from item import Item
from player import Player
from score import Score
from border import Border
from stage import Stage


def view_score(username):
    try:
        with open('game_data.json', 'r') as data_file:
            data_dict = json.load(data_file)
    except FileNotFoundError:
        print(f'No Data Find Found')
    else:
        if username in data_dict:
            color = data_dict[username]['color']
            your_score = data_dict[username]['score']
            print(f'Color: {color}\nScore: {your_score}')
        else:
            print(f'No details for {username} exists.')


while True:
    choice = input('Type (p) to play a game or (v) to view your score or (q) to quit: ').lower()
    if choice == 'p':
        stage = Stage(Border(corner=[-280, -280], height=280, width=280), Screen())
        user_name, user_color = stage.ask_input()
        player = Player(user_name, user_color)
        stage.create_screen(player)
        stage.add_item(10)
        stage.add_obs(7)
        score = Score()
        high_score = Score()
        # score.show_tittle()
        score.update_score(player)
        high_score.show_high_score()
        # obstacle_list = [Obstacle() for i in range(4)]
        while True:
            stage.update_screen()
            player.move()
            for item in stage.items:
                item.move()

                if player.is_collision_item(item):
                    item.jump()
                    score.change_score(100, player)

            for obs in stage.obstacles:
                obs.move()

                if player.is_collision_item(obs):
                    score.save_score(player)
                    stage.end(Score())
    elif choice == 'v':
        username = input('Please type your username you what to view score: ')
        view_score(username)
    elif choice == 'q':
        break
    else:
        print('Please type a valid input.')
