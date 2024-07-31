"""
- JSON of English words is used
- Normal difficulty: words from 5-8 characters and 2-3 blank spaces
- Hard difficulty: 8+ character words and 5 blank spaces
- Single-Player: one person plays
- Pass & Play: 2 players can play and compete to win
- Each round won is +1 score
- 3 health at start of each game, each round lost is -1 health
"""
# Imports
import json
import random
from collections import Counter


# Load Words
with open('words_dictionary.json') as json_file:
    words_data = json.load(json_file)


# Functions
def title_art():
    print("""
    ┏━━━┓━━━━━━┏┓━┏┓━━━━━━━━━━━━━━┏┓┏┓┏┓━━━━━━━━━┏┓━━━━┏━━━┓━━━━━━━━━━━━━
    ┃┏━┓┃━━━━━┏┛┗┓┃┃━━━━━━━━━━━━━━┃┃┃┃┃┃━━━━━━━━━┃┃━━━━┃┏━┓┃━━━━━━━━━━━━━
    ┃┗━┛┃┏┓━┏┓┗┓┏┛┃┗━┓┏━━┓┏━┓━━━━━┃┃┃┃┃┃┏━━┓┏━┓┏━┛┃━━━━┃┃━┗┛┏━━┓━┏┓┏┓┏━━┓
    ┃┏━━┛┃┃━┃┃━┃┃━┃┏┓┃┃┏┓┃┃┏┓┓━━━━┃┗┛┗┛┃┃┏┓┃┃┏┛┃┏┓┃━━━━┃┃┏━┓┗━┓┃━┃┗┛┃┃┏┓┃
    ┃┃━━━┃┗━┛┃━┃┗┓┃┃┃┃┃┗┛┃┃┃┃┃━━━━┗┓┏┓┏┛┃┗┛┃┃┃━┃┗┛┃━━━━┃┗┻━┃┃┗┛┗┓┃┃┃┃┃┃━┫
    ┗┛━━━┗━┓┏┛━┗━┛┗┛┗┛┗━━┛┗┛┗┛━━━━━┗┛┗┛━┗━━┛┗┛━┗━━┛━━━━┗━━━┛┗━━━┛┗┻┻┛┗━━┛
    ━━━━━┏━┛┃━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    ━━━━━┗━━┛━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    """)
    print("Disclaimer: words may be profane due to the file used containing several hundred thousand words")


class GameSelect:
    def __init__(self, mode, difficulty):
        self.mode = mode
        self.difficulty = difficulty


class HealthInit:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

def game_mode_choice(retries_game_mode):
    if retries_game_mode != 1:
        print("Choose Game Mode")
        print("[1] Single-Player")
        print("[2] Pass & Play 2-Player")
    game_mode = int(input("> "))
    if game_mode == 1:
        return game_mode
    elif game_mode == 2:
        return game_mode
    else:
        print("Invalid choice, try again")
        game_mode_choice(1)


def game_difficulty_choice(retries_game_difficulty):
    if retries_game_difficulty != 1:
        print("Choose Game Difficulty")
        print("[1] Normal")
        print("[2] Hard")
    game_difficulty = int(input("> "))
    if game_difficulty == 1:
        return game_difficulty
    elif game_difficulty == 2:
        return game_difficulty
    else:
        print("Invalid choice, try again")
        game_mode_choice(1)


def game_play(mode, difficulty, health_p1, health_p2):
    if mode == 1 & difficulty == 1:
        while health_p1 > 0:
            random_word = random.choice(list(words_data.keys()))
            length = len(random_word)
            if 5 <= length <= 8:
                positions = random.sample(range(len(random_word)),random.randint(2,3))
                characters_in_word = list(random_word)
                for i in positions:
                    characters_in_word[i] = '_'
                replaced_word = ''.join(characters_in_word)
                print(random_word)
                print(replaced_word)
                word_guess = input("Enter your guess: ")
                if word_guess == random_word:
                    print("good job")


# Run Functions
# run function to load words
title_art()
game_mode_return = game_mode_choice(0)
game_difficulty_return = game_difficulty_choice(0)
game = GameSelect(game_mode_return, game_difficulty_return)
health = HealthInit(3, 3)
game_play(game.mode, game.difficulty, health.p1, health.p2)
