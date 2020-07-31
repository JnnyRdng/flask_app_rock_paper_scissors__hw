from app import app
from flask import render_template, request, redirect

@app.route("/")
def hello_world():
    return "Hello, World!"