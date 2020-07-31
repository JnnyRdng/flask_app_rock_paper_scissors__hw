from app import app
from flask import render_template, request, redirect
from app.modules.player import Player
from app.modules.game import Game

@app.route("/")
def home_page():
    return "Rock, Paper, Scissors game!"

@app.route("/<choice1>/<choice2>")
def play_a_game(choice1, choice2):
    game = Game()
    p1 = Player("Player 1", choice1)
    p2 = Player("Player 2", choice2)
    winner = game.play_round(p1, p2)
    if winner is not None:
        loser = p2 if p1 == winner else p1
        return render_template("winner.html", title=f"{winner.name} Wins!", winner=winner, loser=loser)
    else:
        return render_template("draw.html", title="It's a draw!", choice=p1.choice)
        

# @app.route("/paper/rock")
# def paper_beats_rock():
#     return "Player 1 wins playing paper against rock!"

# @app.route("/paper/scissors")
# def paper_loses_scissors():
#     return "Player 1 loses playing paper against scissors!"

# @app.route("/rock/scissors")
# def rock_beats_scissors():
#     return "Player 1 wins playing rock against scissors!"

# @app.route("/rock/paper")
# def rock_loses_paper():
#     return "Player 1 loses playing rock against paper!"

# @app.route("/scissors/paper")
# def scissors_beats_paper():
#     return "Player 1 wins playing scissors against paper!"

# @app.route("/scissors/rock")
# def scissors_loses_rock():
#     return "Player 1 loses playing scissors against rock!"

# @app.route("/paper/paper")
# @app.route("/rock/rock")
# @app.route("/scissors/scissors")
# def draw():
#     return "Draw! No one wins!"


