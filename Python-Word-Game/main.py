"""
- JSON of English words is used
- Normal difficulty: words from 5-8 characters and 1 blank space
- Hard difficulty: 8+ character words and 3 blank spaces
- Single-Player: one person plays
- Pass & Play: 2 players can play and compete to win
- Each round won is +1 score
- 3 health at start of each game, each round lost is -1 health
"""
# Imports
import json
import random
import sys

# Load Words
with open('words_dictionary.json') as json_file:
    words_data = json.load(json_file)


# Classes
class GameSelect:
    def __init__(self, mode, difficulty):
        self.mode = mode
        self.difficulty = difficulty


class HealthInit:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2


class PointsInit:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2


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
    print("Disclaimer: words may be profane due to the word dictionary used containing several hundred thousand words.")


def game_mode_choice(retries_game_mode):
    if retries_game_mode != 1:
        print("Choose Game Mode:")
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
        print("Choose Game Difficulty:")
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


def game_play(mode, difficulty, health_p1, health_p2, points_p1, points_p2):
    if mode == 1 and difficulty == 1:
        while health_p1 > 0:
            random_word = random.choice(list(words_data.keys()))
            length = len(random_word)
            if 5 <= length <= 8:
                positions = random.sample(range(len(random_word)), 1)
                characters_in_word = list(random_word)
                for i in positions:
                    characters_in_word[i] = '_'
                replaced_word = ''.join(characters_in_word)
                print(replaced_word)
                word_guess = input("Enter your guess: ")
                if word_guess == random_word:
                    points_p1 = points_p1 + 1
                    print("Correct!")
                    print("Health:", health_p1, "| Points:", points_p1)
                    print("")
                elif word_guess != random_word:
                    health_p1 = health_p1 - 1
                    print("Incorrect!")
                    print("Correct answer: ", random_word)
                    print("Health:", health_p1, "| Points:", points_p1)
                    print("")
        print("Game Over!")
        print("Points:", points_p1)
        try_again(0)
    elif mode == 1 and difficulty == 2:
        while health_p1 > 0:
            random_word = random.choice(list(words_data.keys()))
            length = len(random_word)
            if 8 <= length:
                positions = random.sample(range(len(random_word)), 3)
                characters_in_word = list(random_word)
                for i in positions:
                    characters_in_word[i] = '_'
                replaced_word = ''.join(characters_in_word)
                print(replaced_word)
                word_guess = input("Enter your guess: ")
                if word_guess == random_word:
                    points_p1 = points_p1 + 1
                    print("Correct!")
                    print("Health:", health_p1, "| Points:", points_p1)
                    print("")
                elif word_guess != random_word:
                    health_p1 = health_p1 - 1
                    print("Incorrect!")
                    print("Correct answer: ", random_word)
                    print("Health:", health_p1, "| Points:", points_p1)
                    print("")
        print("Game Over!")
        print("Points:", points_p1)
        try_again(0)


def try_again(choice):
    print("Try Again? [Y/N]")
    try_again_choice = input("> ")
    if try_again_choice == "Y" or try_again_choice == "y":
        run()
        choice = 1
    if try_again_choice == "N" or try_again_choice == "n":
        sys.exit(0)
    else:
        if choice != 1:
            print("Invalid input.")
            try_again(0)


def run():
    game_mode_return = game_mode_choice(0)
    game_difficulty_return = game_difficulty_choice(0)
    game = GameSelect(game_mode_return, game_difficulty_return)
    health = HealthInit(3, 3)
    points = PointsInit(0, 0)
    game_play(game.mode, game.difficulty, health.p1, health.p2, points.p1, points.p2)


# Run Functions
title_art()
run()
