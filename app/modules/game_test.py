import unittest

from app.modules.game import Game
from app.modules.player import Player


class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        self.player_r = Player("Jim", "rock")
        self.player_p = Player("Jim", "paper")
        self.player_s = Player("Jim", "scissors")

    def test_choices_empty_dict(self):
        expected = {}
        actual = self.game.choices
        self.assertEqual(expected, actual)

    def test_valid_choices(self):
        expected = "paper"
        actual = self.game.valid_choices[1]
        self.assertEqual(expected, actual)

    def test_play_round_paper_beats_rock(self):
        expected = self.player_p
        actual = self.game.play_round(self.player_p, self.player_r)
        self.assertEqual(expected, actual)

    def test_play_round_paper_beats_rock__players_switched(self):
        expected = self.player_p
        actual = self.game.play_round(self.player_r, self.player_p)
        self.assertEqual(expected, actual)

    def test_play_round_paper_loses_scissors(self):
        expected = self.player_s
        actual = self.game.play_round(self.player_p, self.player_s)
        self.assertEqual(expected, actual)

    def test_play_round_paper_loses_scissors__players_switched(self):
        expected = self.player_s
        actual = self.game.play_round(self.player_s, self.player_p)
        self.assertEqual(expected, actual)
    
    def test_play_round_rock_beats_scissors(self):
        expected = self.player_r
        actual = self.game.play_round(self.player_r, self.player_s)
        self.assertEqual(expected, actual)

    def test_play_round_rock_beats_scissors__players_switched(self):
        expected = self.player_r
        actual = self.game.play_round(self.player_s, self.player_r)
        self.assertEqual(expected, actual)

    def test_play_round_draw(self):
        actual = self.game.play_round(self.player_r, self.player_r)
        self.assertIsNone(actual)