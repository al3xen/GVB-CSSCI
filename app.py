from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("landing.html")

@app.route("/about")
def page1():
    return render_template("about_us.html")

@app.route("/rewards")
def page2():
    return render_template("rewards.html")

@app.route("/profile")
def page3():
    return render_template("profile.html")

@app.route("/travel")
def page4():
    return render_template("travelstats.html")

@app.route("/support")
def page5():
    return render_template("support.html")

@app.route("/levels")
def page6():
    return render_template("levels.html")

@app.route("/feedback")
def page7():
    return render_template("feedback.html")

@app.route("/terms")
def page8():
    return render_template("terms.html")
