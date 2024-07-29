'''
- CSV of English words is used
- Normal difficulty: words from 5-15 characters and 1-3 blank spaces
- Hard difficulty: 10+ character words and 5 blank spaces
- Single-Player: one person plays
- Pass & Play: 2 players can play and compete to win
- Each round won is +1 score
- 3 health at start of each game, each round lost is -1 health
'''


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


def game_choice(retries_game_mode):
    if retries_game_mode != 1:
        print("Choose Game Mode")
        print("[1] Single-Player")
        print("[2] Pass & Play 2-Player")
    game_mode = int(input("> "))
    if game_mode == 1:
        single_player()
    elif game_mode == 2:
        two_player()
    else:
        print("Invalid choice, try again")
        retries_game_mode = 1
        game_choice(1)


def single_player():
    print("Single-Player")


def two_player():
    print("Single-Player")

# Run Functions
title_art()
game_choice(0)
