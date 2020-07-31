from app import app
from flask import render_template, request, redirect

@app.route("/")
def home_page():
    return "Rock, Paper, Scissors game!"

@app.route("/paper/rock")
def paper_beats_rock():
    return "Player 1 wins playing paper against rock!"

@app.route("/paper/scissors")
def paper_loses_scissors():
    return "Player 1 loses playing paper against scissors!"

@app.route("/rock/scissors")
def rock_beats_scissors():
    return "Player 1 wins playing rock against scissors!"

@app.route("/rock/paper")
def rock_loses_paper():
    return "Player 1 loses playing rock against paper!"

@app.route("/scissors/paper")
def scissors_beats_paper():
    return "Player 1 wins playing scissors against paper!"

@app.route("/scissors/rock")
def scissors_loses_rock():
    return "Player 1 loses playing scissors against rock!"

@app.route("/paper/paper")
@app.route("/rock/rock")
@app.route("/scissors/scissors")
def draw():
    return "Draw! No one wins!"


