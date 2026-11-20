import random
from words import WORDS


def choose_word():
    return random.choice(WORDS)


if __name__ == "__main__":
    secret_word = choose_word()
    print("Загаданное слово:", secret_word)
