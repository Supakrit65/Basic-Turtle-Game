from turtle import Turtle
from player import Player
import json


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.color('#900C3F')
        self.score = 0
        self.old_high_score = 0

    def show_high_score(self):
        try:
            with open('game_data.json', 'r') as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            self.write('High score: 0', False, align='right', font=("Comic Sans MS", 14, "normal"))
        else:
            scores = []
            for each_dict in data.values():
                scores.append(each_dict['score'])
            high_score = max(scores)
            self.goto(270, 290)
            self.write(f'High score: {high_score}', False, align='right', font=("Comic Sans MS", 12, "normal"))

    @staticmethod
    def get_high_score():
        try:
            with open('game_data.json', 'r') as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            return 0
        else:
            scores = []
            for each_dict in data.values():
                scores.append(each_dict['score'])
            high_score = max(scores)
            return int(high_score)

    def update_score(self, player):
        self.clear()
        self.goto(-280, 290)
        self.write(f'Score: {self.score}', False, align='left', font=("Comic Sans MS", 14, "normal"))
        # update player score
        player.score = self.score

    def change_score(self, points, player):
        self.score += points
        self.update_score(player)

    @staticmethod
    def save_score(player):
        new_data = {
            player.name: {
                'color': player.colour,
                'score': player.score
            }
        }
        try:
            with open('game_data.json', 'r') as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open('game_data.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open('game_data.json', 'w') as data_file:
                json.dump(data, data_file, indent=4)

