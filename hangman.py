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


def print_hangman(lives):
    print(stages(lives))

def check(guess, secret, already_guessed,lives):
    if guess in secret:
        already_guessed.append(guess)
    else:
        lives -= 1

    word = ""
    for i in secret:
        if i in already_guessed:
            word += i
        else:
            word += "_"

    return word

def win(dis,secret):
    if dis == secret:
        return True
    return False


def game_loop():
    ch = choose_word()
    print(ch)
    displayed = parse_secret(ch)
    print(displayed)
    lives = 6
    alg = [] #pozor kde davas premeene vo while slucke sa resetuje
    game_over = False
    print_logo()

    while not game_over:
        g = player_guess()
        displayed = check(g, ch, alg,lives)
        print(displayed)

        if lives == 0:
            print("Prehral si!")
            game_over = True

        if win(displayed,ch):
            print("Vyhral si!")
            game_over = True

