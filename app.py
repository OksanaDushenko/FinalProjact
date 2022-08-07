import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configure application
app = Flask(__name__)


# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///webDB.db")

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route('/portrets')
def portrets():
    return render_template('portrets.html')

@app.route('/nature')
def nature():
    return render_template('nature.html')

@app.route('/architecture')
def architecture():
    return render_template('architecture.html')

@app.route('/product')
def product():
    return render_template('product.html')


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        #access form data
        username = request.form.get("username")
        email = request.form.get("email")
        feedback = request.form.get("feedback")

        #insert data into database
        db.execute("INSERT INTO FeedbackTable (UserName, Email, Feedback) VALUES(?, ?, ?)", username, email, feedback)

        #go back to homepage
        return redirect("/")

    else:

        #rander main page
        return render_template("page1.html")

if __name__ == '__main__':
    app.run()