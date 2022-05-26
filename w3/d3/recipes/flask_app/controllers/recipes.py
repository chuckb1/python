from flask_app import app
from flask_app.models.recipe import Recipe
from flask_app.models.user import User
from flask import render_template, request, redirect, session, flash


# this route pulls up the create recipe page
@app.route('/create/recipe/page')
def create_recipe_page():
    if "user_id" not in session:
        flash("Please register or login before entering our site!!")
        return redirect('/')    
    logged_user = Recipe.get_all_recipes()
    return render_template("create_recipe.html", user = logged_user)

# this route will create the recipe
@app.route('/create/recipe', methods = ['POST'])
def create_the_recipe():
    if not Recipe.validate_recipe(request.form):
        return redirect('/create/recipe/page')
    data = {
        'name' : request.form['name'],
        'under_30' : request.form['under_30'], 
        'id' : session['user_id'],
        'description' : request.form['description'],
        'instructions' : request.form['instructions']
    }
    Recipe.create_this_recipe(data)
    return redirect('/dashboard')

@app.route('/show/<int:recipe_id>')
def show_recipe(recipe_id):
    data = {
        'id' : recipe_id
    }
    recipe = Recipe.show_recipe(data)
    logged_user = User.get_by_id({'id': session['user_id']})
    return render_template("show_recipe.html", recipe = recipe, user = logged_user)

# this route pulls up the edit recipe page
@app.route('/edit/recipe/<int:recipe_id>')
def edit_recipe_form(recipe_id):
    data = {
        "id" : recipe_id
    }
    recipe = Recipe.show_recipe(data)
    return render_template("edit_recipe.html", recipe = recipe)

# this route will edit the recipe
@app.route('/update/recipe/<int:recipe_id>', methods = ['POST'])
def edit_recipe(recipe_id):
    if not Recipe.validate_recipe(request.form):
        return redirect('/edit/recipe/' + str(recipe_id))
    data = {
        'id' : recipe_id,
        'name' : request.form['name'],
        'under_30' : request.form['under_30'], 
        'description' : request.form['description'],
        'instructions' : request.form['instructions']
    }
    print(data)
    Recipe.edit_recipe(data)
    return redirect('/dashboard')



@app.route('/delete/<int:recipe_id>')
def delete_recipe(recipe_id):
    data = {
        "id" : recipe_id
    }
    Recipe.delete_recipe(data)
    return redirect('/dashboard')


