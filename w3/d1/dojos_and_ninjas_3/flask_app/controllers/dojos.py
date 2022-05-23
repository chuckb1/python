from flask_app import app
from flask_app.models.dojo import Dojo
from flask import render_template, request, redirect, session

@app.route("/dojos")
def dojos_index():
    # call the get all classmethod to get all friends
    dojos = Dojo.get_all_dojos()
    print(dojos)
    return render_template("create_dojo.html", dojos = dojos)


@app.route('/create/dojo', methods = ["POST"])
def create_dojo():
    data = {
        'name': request.form['name'],
    }
    Dojo.create_dojo(data)
    return redirect('/dojos')