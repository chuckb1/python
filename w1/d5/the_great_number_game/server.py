from flask import Flask,render_template, redirect, session, request
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'
import random


@app.route('/')
def random_number():
    if "number" not in session:
        session["number"] = random.randint(1,100)
    
    return render_template("index.html")

@app.route('/submit', methods = ["POST"])
def submit():
    session["guess"] = int(request.form["guess"])
    return redirect('/')

@app.route('/reset')
def reset():
        session.clear()
        return redirect('/')


if __name__ == "__main__":
        app.run(debug=True)