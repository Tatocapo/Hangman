import random
from hangman_art import logo
from hangman_words import word_list

def print_logo():
    print(logo)

def choose_word():
    ch = random.choice(word_list)
    return ch

def parse_secret(ch):
    p = ""
    for i in range(len(ch)):
        p += "_"
    return p

def player_guess():

def game_loop():
    ch = choose_word()
    pars = parse_secret(ch)
    lives = 6
    game_over = True
    print_logo()
    while not game_over:




