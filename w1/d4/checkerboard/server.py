from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')


@app.route('/<int:x>')
def how_big(x = 4):
    return render_template("index.html", x = x)

if __name__ == "__main__":
        app.run(debug=True)

