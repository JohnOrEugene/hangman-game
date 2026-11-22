
"""
Основной модуль игры «Виселица».
Содержит функции выбора слова, его отображения
и проверки введённых букв.
"""
import random
from words import WORDS

def choose_word():
    """
    Выбирает случайное слово из списка WORDS.

    Returns:
        str: случайно выбранное слово.
    """
    return random.choice(WORDS)

def display_word(secret_word, guessed_letters):
    """
    Формирует отображение загаданного слова.
    Угаданные буквы показываются, остальные заменяются
    символом подчёркивания.
    Args:
        secret_word (str): загаданное слово.
        guessed_letters (set): множество угаданных букв.
    Returns:
        str: строка со скрытыми и открытыми буквами.
    """
    displayed_word = []

    for letter in secret_word:
        if letter in guessed_letters:
            displayed_word.append(letter)
        else:
            displayed_word.append("_")

    return " ".join(displayed_word)

def is_letter_in_word(secret_word, letter):
    """
    Проверяет наличие введённой буквы в загаданном слове.
    Args:
        secret_word (str): загаданное слово.
        letter (str): проверяемая буква.
    Returns:
        bool: True, если буква есть в слове, иначе False.
    """
    return letter in secret_word

if __name__ == "__main__":
    secret_word = choose_word()
    guessed_letters = set()
    print("Загаданное слово:", display_word(secret_word, guessed_letters))
