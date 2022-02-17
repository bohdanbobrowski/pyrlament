from flask import Flask, render_template
from pyrlament import SeatsGenerator

app = Flask(__name__)


@app.route("/")
def main():
    seats_generator = SeatsGenerator()
    return render_template("home.html", seats=seats_generator.get_seats())
