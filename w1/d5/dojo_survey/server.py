from flask import Flask,render_template, redirect, session, request
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    return render_template("index.html")



@app.route('/process', methods = ["POST", "GET"])
def process():
    session["fName"] = request.form["fName"]
    session["location"] = request.form["location"]
    session["fLanguage"] = request.form["fLanguage"]
    session["comment"] = request.form["comment"]
    return redirect('/result')

@app.route('/result')
def result():
    return render_template("index1.html")

@app.route('/go_back')
def go_back():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
        app.run(debug=True)