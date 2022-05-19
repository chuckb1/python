from flask import Flask, render_template, request, redirect
# import the class from friend.py
from users import User
app = Flask(__name__)

@app.route("/users")
def index():
    # call the get all classmethod to get all friends
    users = User.get_all()
    print(users)
    return render_template("Read(All).html", users = users)
            
@app.route('/create/user')
def user_form():
    return render_template("Create.html")

@app.route('/insert/user', methods = ["POST"])
def create():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    User.create_user(data)
    return redirect('/users')

if __name__ == "__main__":
    app.run(debug=True)
