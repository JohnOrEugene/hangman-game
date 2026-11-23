"""
Основной модуль игры «Виселица».
Содержит функции выбора слова, его отображения,
проверки введённых букв и управления игровым процессом.
"""

import random
from words import WORDS

## Алфавит, допустимый для ввода в игре.
RUSSIAN_ALPHABET = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
## Начальное количество попыток игрока.
MAX_ATTEMPTS = 6

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
        guessed_letters (set): множество введённых букв.
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

def update_attempts(secret_word, letter, remaining_attempts):
    """
    Обновляет количество оставшихся попыток.
    Если введённой буквы нет в загаданном слове,
    количество попыток уменьшается на единицу.
    Args:
        secret_word (str): загаданное слово.
        letter (str): введённая буква.
        remaining_attempts (int): текущее количество попыток.
    Returns:
        int: обновлённое количество оставшихся попыток.
    """
    if not is_letter_in_word(secret_word, letter):
        remaining_attempts -= 1

    return remaining_attempts

def validate_letter(user_input, guessed_letters):
    """
    Проверяет корректность введённой пользователем буквы.
    Проверяет, что введена ровно одна буква русского алфавита
    и что эта буква ещё не использовалась.
    Args:
        user_input (str): строка, введённая пользователем.
        guessed_letters (set): множество ранее введённых букв.
    Returns:
        tuple: пара значений (буква, сообщение об ошибке).
            При корректном вводе возвращается (буква, None).
            При некорректном вводе возвращается (None, сообщение).
    """
    letter = user_input.strip().lower()

    if not letter:
        return None, "Вы ничего не ввели. Введите одну букву."

    if len(letter) != 1:
        return None, "Введите ровно одну букву."

    if letter not in RUSSIAN_ALPHABET:
        return None, "Можно вводить только буквы русского алфавита."

    if letter in guessed_letters:
        return None, f"Букву «{letter}» вы уже вводили."

    return letter, None

def is_game_won(secret_word, guessed_letters):
    """
    Проверяет, угадал ли игрок все буквы загаданного слова.
    Args:
        secret_word (str): загаданное слово.
        guessed_letters (set): множество введённых игроком букв.
    Returns:
        bool: True, если все буквы слова угаданы, иначе False.
    """
    return all(letter in guessed_letters for letter in secret_word)

def is_game_lost(remaining_attempts):
    """
    Проверяет, закончились ли у игрока попытки.
    Args:
        remaining_attempts (int): количество оставшихся попыток.
    Returns:
        bool: True, если попыток не осталось, иначе False.
    """
    return remaining_attempts <= 0


def play_game():
    """
    Запускает одну партию игры «Виселица».
    Управляет игровым процессом: принимает буквы,
    обновляет количество попыток и проверяет завершение игры.
    """
    secret_word = choose_word()
    guessed_letters = set()
    remaining_attempts = MAX_ATTEMPTS
    print("Добро пожаловать в игру «Виселица»!")
    print("Загаданное слово:", display_word(secret_word, guessed_letters))
    print(f"Количество попыток: {remaining_attempts}")

    while not is_game_won(secret_word, guessed_letters) and not is_game_lost(remaining_attempts):
        user_input = input("\nВведите букву: ")

        letter, error_message = validate_letter(user_input, guessed_letters)

        if error_message is not None:
            print(error_message)
            continue

        guessed_letters.add(letter)
        remaining_attempts = update_attempts(secret_word, letter, remaining_attempts)

        if is_letter_in_word(secret_word, letter):
            print(f"Есть такая буква: «{letter}»!")
        else:
            print(f"Буквы «{letter}» нет в загаданном слове.")

        print("Загаданное слово:", display_word(secret_word, guessed_letters))
        print(f"Осталось попыток: {remaining_attempts}")

    if is_game_won(secret_word, guessed_letters):
        print(f"\nПоздравляем! Вы угадали слово: {secret_word}")
    else:
        print(f"\nПопытки закончились. Вы проиграли!")
        print(f"Загаданное слово было: {secret_word}")

if __name__ == "__main__":
    play_game()