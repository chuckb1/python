from flask_app import app
from flask_app.models.user import User
from flask_app.models.recipe import Recipe
from flask import render_template, request, redirect, session, flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def register_user_form():
    User.get_all_users()
    return render_template("login_register.html")

@app.route('/register/user', methods = ['POST'])
def register_this_user():    
    data = {
        'email' : request.form['email'],
    }
    user_in_db = User.get_by_email(data)
    if user_in_db:
        flash("Email is already in use")
        return redirect('/')
    if User.validate_user(request.form):
        pw_hash = bcrypt.generate_password_hash(request.form['password'])
        data = {
            'first_name' : request.form['first_name'],
            'last_name' : request.form['last_name'],
            'email' : request.form['email'],
            "password" : pw_hash
        }
        user_id = User.register_user(data)
        session['user_id'] = user_id
        return redirect('/')
    return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    # see if the username provided exists in the database
    data = { "email" : request.form["email"] }
    user_in_db = User.get_by_email(data)    
    if not user_in_db: # user is not registered in the db
        flash("Invalid Email/Password")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']): # if we get False after checking the password        
        flash("Invalid Email/Password")
        return redirect('/')    
    session['user_id'] = user_in_db.id # if the passwords matched, we set the user_id into session    
    return redirect("/dashboard") # never render on a post!!!

@app.route('/dashboard')
def dashboard():
    if "user_id" not in session:
        flash("Please register or login before entering our site!!")
        return redirect('/')
    data = {
        'id' : session['user_id'],
    }
    logged_user = User.get_by_id(data) 
    recipes = Recipe.get_all_recipes()   
    return render_template('dashboard.html', recipes = recipes, user = logged_user)

@app.route('/log_out')
def log_out():
    session.clear()
    return redirect('/')

