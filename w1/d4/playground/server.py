from flask import Flask,render_template
app = Flask(__name__)

@app.route('/play/<int:x>/<string:color1>')
def play(x, color1):
    return render_template("index.html", x = x, color1 = color1)



if __name__ == "__main__":
        app.run(debug=True)