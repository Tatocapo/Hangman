import random
from hangman_art import logo,stages
from hangman_words import word_list

def print_logo():
    print(logo)

def choose_word():
    ch = random.choice(word_list)
    return ch

def parse_secret(secret):
    p = ""
    for i in range(len(secret)):
        p += "_"
    return p

def player_guess():
    p_in = input("Enter guess: ").lower()
    if len(p_in) != 1 or  not p_in.isalpha():
        print("Enter valid character")
    return p_in

def check_guess(guess, secret):
    for i in secret:
        if i == guess:
            print("Your guess was right.")
        else:
            print("Your guess was wrong")

def decrease_lives(live):
    live -= 1

def print_hangman(lives):
    print(stages(lives))

def game_loop():
    ch = choose_word()
    p = parse_secret(ch)
    correct_letter = []
    print(ch)
    lives = 6
    game_over = False
    print_logo()
    while not game_over:
        check_guess(player_guess(),ch)





