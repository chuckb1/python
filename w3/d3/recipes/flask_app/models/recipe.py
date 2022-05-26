from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

from flask_app.models import user

class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.under_30 = data['under_30']
        self.description = data['description']
        self.instructions = data['instructions']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        self.user = {}

    @classmethod
    def get_all_recipes(cls):
        query = "SELECT * FROM recipes LEFT JOIN users ON users.id = recipes.users_id;"
        results = connectToMySQL('recipes_schema').query_db(query)
        recipes = []
        for row in results:
            recipe = cls(row)
            user_data = {
                "id" : row['users_id'],
                "first_name" : row['first_name'],
                "last_name" : row['last_name'],
                "email"  :   row['email'],
                "password" : row['password']
            }
            recipe.user = user.User(user_data)
            recipes.append(recipe)
            print(recipe.user.id)
        return recipes

    @classmethod
    def create_this_recipe(cls,data):
        query = "INSERT INTO recipes(name,under_30, users_id, description, instructions) VALUES(%(name)s, %(under_30)s, %(id)s, %(description)s, %(instructions)s)"
        results = connectToMySQL('recipes_schema').query_db(query,data)
        return results
    
    @classmethod
    def show_recipe(cls,data):
        query = "SELECT * FROM recipes WHERE id = %(id)s"
        results = connectToMySQL('recipes_schema').query_db(query, data)
        return cls(results[0])

    @classmethod
    def edit_recipe(cls, data):
        query = "UPDATE recipes SET name = %(name)s, description = %(description)s, instructions = %(instructions)s WHERE id = %(id)s"
        print(query)
        results = connectToMySQL('recipes_schema').query_db(query, data)
        return results

    @classmethod
    def delete_recipe(cls, data):
        query = "DELETE FROM recipes WHERE id = %(id)s"
        return  connectToMySQL('recipes_schema').query_db(query, data)


    @staticmethod
    def validate_recipe(data):
        is_valid = True
        if len(data['name']) < 2:
            flash("Recipe name must be at least 2 characters.")
            is_valid = False
        if len(data['description']) < 2:
            flash("Description name must be at least 2 characters.")
            is_valid = False
        if len(data['instructions']) < 2:
            flash("Instructions name must be at least 2 characters.")
            is_valid = False
        return is_valid