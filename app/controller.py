from app import app
from flask import render_template, request, redirect

@app.route("/")
def hello_world():
    return "Rock, Paper, Scissors game!"

@app.route("/paper/rock")
def paper_beats_rock():
    return "Player 1 wins playing paper against rock!"

@app.route("/rock/scissors")
def rock_beats_scissors():
    return "Player 1 wins playing rock against scissors!"

@app.route("/scissors/paper")
def scissors_beats_paper():
    return "Player 1 wins playing scissors against paper!"

@app.route("/paper/paper")
@app.route("/rock/rock")
@app.route("/scissors/scissors")
def draw():
    return "Draw! No one wins"


