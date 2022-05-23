from flask_app import app
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo
from flask import render_template, request, redirect, session

@app.route("/ninjas")
def create_ninja_form():
    # call the get all classmethod to get all friends
    dojos = Dojo.get_all_dojos()
    return render_template("create_ninja.html", dojos = dojos,)

@app.route('/create/ninja', methods = ["POST"])
def create_ninja():
    data = {
        'first_name': request.form['first_name'],
        'last_name' : request.form['last_name'],
        'age' : request.form['age'],
        'dojo_id' : request.form['dojo_id'],
    }
    Ninja.create_ninja(data)
    return redirect('/dojos')

@app.route("/dojos/<int:dojo_id>")
def show_dojo(dojo_id):
    data = {
        "id" : dojo_id
    }
    dojo = Dojo.show_dojo(data)
    return render_template("show_dojo.html", dojo = dojo)