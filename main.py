import flask
from flask import Flask, render_template


app = Flask(__name__,template_folder="templates",static_folder="static")


@app.route("/")
def home():
    return render_template('home.html')

@app.route("/resume/")
def resume():
    return flask.redirect("https://rebrand.ly/kevsilver_resume")


if __name__ == '__main__':
    app.run(debug=True)