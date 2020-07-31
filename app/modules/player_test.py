import unittest

from app.modules.player import Player


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player_no_choice = Player("Jeff")
        self.player_choice = Player("Geoff", "rock")

    def test_player_no_choice_instantiated(self):
        expected = ""
        actual = self.player_no_choice.choice
        self.assertEqual(expected, actual)
