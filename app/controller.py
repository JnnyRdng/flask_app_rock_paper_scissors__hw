from app import app
from flask import render_template, request, redirect
from app.modules.player import Player
from app.modules.logic import game, cpu, player, player_name, sort_scores


@app.route("/")
def home_page():
    return render_template("welcome.html", title="Home", player_name=player_name)


@app.route("/play")
def play_game():
    return render_template("play.html", title="Play", player_name=player_name)


@app.route("/about")
def about_page():
    return render_template("about.html", title="About")


@app.route("/set-name", methods=["POST"])
def get_player_name():
    global player_name
    new_name = request.form["name"]
    player_name = new_name if new_name != "" else player_name
    return redirect("/play")


@app.route("/<choice1>/<choice2>")
def play_a_game(choice1, choice2):
    p1 = Player("Player 1", choice1)
    p2 = Player("Player 2", choice2)
    winner = game.play_round(p1, p2)
    return route_winner(winner, p1, p2)


@app.route("/get-choices", methods=["POST"])
def get_choices():
    move = request.form["move"]
    player.name = player_name
    player.choice = move
    game.decide_cpu_move(cpu)
    winner = game.play_round(player, cpu)
    return route_winner(winner, player, cpu)


@app.route("/reset-scores")
def reset_scoreboard():
    player.score = 0
    cpu.score = 0
    return redirect("/play")


def route_winner(winner, player, cpu):
    if winner == False:
        return redirect("/")
    elif winner is None:
        scores = sort_scores()
        return render_template(
            "draw.html", title="It's a draw!", choice=player.choice, scores=scores
        )
    else:
        winner.score += 1
        scores = sort_scores()
        if winner == player:
            return render_template(
                "winner.html",
                title=f"{player.name} Wins!",
                winner=player,
                loser=cpu,
                scores=scores,
            )
        elif winner == cpu:
            return render_template(
                "loser.html",
                title=f"You lost!",
                winner=cpu,
                loser=player,
                scores=scores,
            )
