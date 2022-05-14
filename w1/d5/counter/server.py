from flask import Flask,render_template, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'


@app.route('/')
def count_click():
        if 'count' in session:
                session["count"] += 1
        else:
                session["count"] = 1
        
        return render_template("index.html")

@app.route('/twosessions')
def count_click_two():
        if 'count' in session:
                session["count"] += 1
        else:
                session["count"] = 1
        
        return redirect('/')

@app.route('/destroy_session')
def destroy_session():
        session.clear()
        return redirect('/')



if __name__ == "__main__":
        app.run(debug=True)