from app.modules.game import Game
from app.modules.player import Player


game = Game()
player_name = "Player"
player = Player(player_name, "rock")
cpu = Player("Computer", "rock")

