from app import app
from flask import render_template, request, redirect
from app.modules.player import Player
from app.modules.game import Game


@app.route("/")
def home_page():
    return render_template("index.html", title="Home")


@app.route("/<choice1>/<choice2>")
def play_a_game(choice1, choice2):
    game = Game()
    p1 = Player("Player 1", choice1)
    p2 = Player("Player 2", choice2)
    winner = game.play_round(p1, p2)
    if winner == False:
        return redirect("/")
    elif winner is not None:
        loser = p2 if p1 == winner else p1
        return render_template(
            "winner.html", title=f"{winner.name} Wins!", winner=winner, loser=loser
        )
    else:
        return render_template("draw.html", title="It's a draw!", choice=p1.choice)

@app.route("/get-choices", methods=["POST"])
def get_choices():
    return request.form["move"]