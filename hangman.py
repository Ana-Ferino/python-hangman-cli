import random


def print_opening_message():
    print("\n*********************************")
    print("***Welcome to the Hangman Game!***")
    print("*********************************\n")


def play_hangman():

    print_opening_message()
    secret_word = load_secret_word()

    guessed_letters = initialize_guessed_letters(secret_word)
    print(guessed_letters)

    hung = False
    won = False
    errors = 0

    while not won and not hung:

        guess = ask_for_guess()

        if guess in secret_word:
            mark_correct_guess(guess, guessed_letters, secret_word)
        else:
            errors += 1
            draw_hangman(errors)

        hung = errors == 7
        won = "_" not in guessed_letters
        print(guessed_letters)

    if won:
        print_victory_message()
    else:
        print_loss_message(secret_word)

    print("\nEnd of the game")


def load_secret_word():
    file = open("words.txt", "r")
    words = []

    for line in file:
        line = line.strip()
        words.append(line)

    file.close()

    number = random.randrange(0, len(words))
    secret_word = words[number].upper()

    return secret_word


def initialize_guessed_letters(word):
    return ["_" for letter in word]


def ask_for_guess():
    guess = input("\nGuess a letter: ")
    guess = guess.strip().upper()

    return guess


def mark_correct_guess(guess, guessed_letters, secret_word):
    index = 0
    for letter in secret_word:
        if guess == letter:
            guessed_letters[index] = letter
        index += 1


def draw_hangman(errors):
    print("  _______     ")
    print(" |/      |    ")

    if errors == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if errors == 2:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if errors == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if errors == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if errors == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if errors == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if errors == 7:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def print_victory_message():
    print("Congratulations, you won!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def print_loss_message(secret_word):
    print("\n\nOops, you were hanged!")
    print(f"The word was {secret_word}")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


if __name__ == '__main__':
    play_hangman()
