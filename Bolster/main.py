import flask
from flask import render_template
app = flask.Flask(__name__)

@app.route('/')
def home():
    return render_template("main.html")


@app.route("/profile")
def profile():
    return render_template("profile.html")

@app.route("/filter")
def filter():
    return render_template("filter.html")

@app.route("/map")
def map():
    return render_template("map.html")

@app.route("/rate")
def rate():
    print ("hello world")
    
    return render_template("rate.html")



if __name__ == '__main__':
    app.run(debug=True)