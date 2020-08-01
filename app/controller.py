from app import app
from flask import render_template, request, redirect
from app.modules.player import Player
from app.modules.logic import game, cpu, player, player_name


@app.route("/")
def home_page():
    return render_template("welcome.html", title="Home", player_name=player_name)


@app.route("/play")
def play_game():
    return render_template("index.html", title="Play!")


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
    print(player_name)
    move = request.form["move"]
    player.name = player_name
    player.choice = move
    game.decide_cpu_move(cpu)
    winner = game.play_round(player, cpu)
    return route_winner(winner, player, cpu)


def route_winner(winner, player, cpu):
    sorted_scores = []
    if player.score >= cpu.score:
        sorted_scores.append(player)
        sorted_scores.append(cpu)
    else:
        sorted_scores.append(cpu)
        sorted_scores.append(player)
    if winner == False:
        return redirect("/")
    elif winner == player:
        player.score += 1
        return render_template(
            "winner.html", title=f"{player.name} Wins!", winner=player, loser=cpu, scores=sorted_scores
        )
    elif winner == cpu:
        cpu.score += 1
        return render_template(
            "loser.html", title=f"You lost!", winner=cpu, loser=player, scores=sorted_scores
        )
    else:
        return render_template("draw.html", title="It's a draw!", choice=player.choice, scores=sorted_scores)
