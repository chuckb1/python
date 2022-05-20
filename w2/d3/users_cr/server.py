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

@app.route('/show/<int:user_id>')
def show_user(user_id):
    data = {
        "id" : user_id
    }
    user = User.show_user(data)
    return render_template("Show_user.html", one_user = user)

@app.route('/edit/user', methods = ["POST"])
def edit_user():
    data = {
        'id' : request.form["id"],
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    User.edit_user(data)
    return redirect('/users')

@app.route('/edit/user/<int:user_id>')
def show_edit_form(user_id):
    data = {
        "id" : user_id
    }
    user = User.show_user(data)
    return render_template("Edit_user.html", user = user)

@app.route('/delete/<int:user_id>')
def delete_user(user_id):
    data = {
        "id" : user_id
    }
    User.delete_user(data)
    return redirect('/users')


if __name__ == "__main__":
    app.run(debug=True)
