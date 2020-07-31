import unittest

from app.modules.game import Game


class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_choices_empty_dict(self):
        expected = {}
        actual = self.game.choices
        self.assertEqual(expected, actual)

    def test_valid_choices(self):
        expected = "paper"
        actual = self.game.valid_choices[1]
        self.assertEqual(expected, actual)
