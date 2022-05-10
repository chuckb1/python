from flask import Flask,render_template
app = Flask(__name__)


@app.route("/")
def index():
    return "hello World"

@app.route("/success")
def success():
    return render_template("index.html")

@app.route("/dojo")
def dojo():
    return "Dojo"

@app.route('/say/<person>')
def hi(person):
    return f"hi {person}"

@app.route('/repeat/<person>/<int:times>')
def repeat(person,times):
    return f"Hello {person * times}"




if __name__ == "__main__":
        app.run(debug=True)

