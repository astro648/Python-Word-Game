"""
- CSV of English words is used
- Normal difficulty: words from 5-15 characters and 1-3 blank spaces
- Hard difficulty: 10+ character words and 5 blank spaces
- Single-Player: one person plays
- Pass & Play: 2 players can play and compete to win
- Each round won is +1 score
- 3 health at start of each game, each round lost is -1 health
"""


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


class GameSelect:
    def __init__(self, mode, difficulty):
        self.mode = mode
        self.difficulty = difficulty


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


# Run Functions
title_art()
game_mode_return = game_mode_choice(0)
game_difficulty_return = game_difficulty_choice(0)
game = GameSelect(game_mode_return, game_difficulty_return)
