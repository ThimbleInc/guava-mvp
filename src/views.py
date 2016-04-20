from flask import render_template
from models.recipe_set import RecipeSet
from models.recipe import Recipe
from src import app

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/recipe-sets')
def recipe_sets():
	rs = RecipeSet()
	return render_template('recipe-sets.html', recipe_sets=rs.sets)

@app.route('/set/id/<int:set_id>')
def set(set_id):
	recipes = Recipe()
	return render_template('set.html', set= recipes.recipes[set_id])

	return 'Set ID is ' + str(set_id)

@app.route('/ingredients/<username>')
def ingredients(username):
	return 'Ingredients for ' + username

