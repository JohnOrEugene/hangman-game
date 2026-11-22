import random
from words import WORDS


def choose_word():
    return random.choice(WORDS)


def display_word(secret_word, guessed_letters):
    displayed_word = []

    for letter in secret_word:
        if letter in guessed_letters:
            displayed_word.append(letter)
        else:
            displayed_word.append("_")

    return " ".join(displayed_word)


if __name__ == "__main__":
    secret_word = choose_word()
    guessed_letters = set()
    print("Загаданное слово:", display_word(secret_word, guessed_letters))
