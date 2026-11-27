"""
Модуль автоматизированных тестов игры «Виселица».
Проверяет работу основных функций из main.py.
"""

import unittest

from main import (
    choose_word,
    display_word,
    is_letter_in_word,
    update_attempts,
    validate_letter,
    is_game_won,
    is_game_lost
)

from words import WORDS

class TestHangman(unittest.TestCase):
    """Набор тестов основных функций игры."""

    def test_choose_word(self):
        """Проверяет, что выбирается слово из списка."""
        self.assertIn(choose_word(), WORDS)

    def test_display_word_hidden(self):
        """Проверяет отображение полностью скрытого слова."""
        self.assertEqual(display_word("арбуз", set()), "_ _ _ _ _")

    def test_display_word_partially_opened(self):
        """Проверяет отображение частично открытых букв."""
        self.assertEqual(display_word("арбуз", {"а", "у"}), "а _ _ у _")

    def test_display_word_fully_opened(self):
        """Проверяет отображение полностью открытого слова."""
        self.assertEqual(display_word("арбуз", {"а", "р", "б", "у", "з"}), "а р б у з")

    def test_letter_exists(self):
        """Проверяет наличие буквы в загаданном слове."""
        self.assertTrue(is_letter_in_word("арбуз", "а"))

    def test_letter_does_not_exist(self):
        """Проверяет отсутствие буквы в загаданном слове."""
        self.assertFalse(is_letter_in_word("арбуз", "к"))

    def test_correct_letter_does_not_reduce_attempts(self):
        """Проверяет, что за правильную букву попытки не уменьшаются."""
        self.assertEqual(update_attempts("арбуз", "а", 6), 6)

    def test_wrong_letter_reduces_attempts(self):
        """Проверяет уменьшение попыток за неправильную букву."""
        self.assertEqual(update_attempts("арбуз", "к", 6), 5)

    def test_validate_correct_letter(self):
        """Проверяет принятие корректной буквы."""
        self.assertEqual(validate_letter("а", set()), ("а", None))

    def test_validate_uppercase_letter(self):
        """Проверяет обработку заглавной буквы и пробелов."""
        self.assertEqual(validate_letter(" А ", set()), ("а", None))

    def test_validate_empty_input(self):
        """Проверяет отклонение пустого ввода."""
        letter, error = validate_letter("", set())

        self.assertIsNone(letter)
        self.assertIsNotNone(error)

    def test_validate_multiple_characters(self):
        """Проверяет отклонение нескольких символов."""
        letter, error = validate_letter("аб", set())

        self.assertIsNone(letter)
        self.assertIsNotNone(error)

    def test_validate_non_russian_character(self):
        """Проверяет отклонение цифры и латинской буквы."""
        for value in ["5", "a"]:
            with self.subTest(value=value):
                letter, error = validate_letter(value, set())

                self.assertIsNone(letter)
                self.assertIsNotNone(error)

    def test_validate_repeated_letter(self):
        """Проверяет отклонение уже использованной буквы."""
        letter, error = validate_letter("а", {"а"})

        self.assertIsNone(letter)
        self.assertIsNotNone(error)

    def test_game_won(self):
        """Проверяет определение победы."""
        self.assertTrue(
            is_game_won("арбуз", {"а", "р", "б", "у", "з"})
        )

    def test_game_not_won(self):
        """Проверяет отсутствие победы, если остались закрытые буквы."""
        self.assertFalse(
            is_game_won("арбуз", {"а", "р", "б", "у"})
        )

    def test_game_lost(self):
        """Проверяет определение поражения при нуле попыток."""
        self.assertTrue(is_game_lost(0))

    def test_game_not_lost(self):
        """Проверяет, что игрок ещё не проиграл при наличии попыток."""
        self.assertFalse(is_game_lost(3))

if __name__ == "__main__":
    unittest.main()
