from app.modules.game import Game
from app.modules.player import Player


game = Game()
player_name = "Player"
player = Player(player_name, "rock")
cpu = Player("Computer", "rock")

def sort_scores():
    sorted_scores = []
    if player.score >= cpu.score:
        sorted_scores.append(player)
        sorted_scores.append(cpu)
    else:
        sorted_scores.append(cpu)
        sorted_scores.append(player)
    return sorted_scores