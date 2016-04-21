from flask import render_template, session, request, redirect, url_for
from models.recipe_set import RecipeSet
from models.recipe import Recipe
from models.user_ingredients import UserIngredients
from src import app

@app.route('/')
def home():
	if 'name' in session:
		return redirect(url_for('ingredients', username=session['name']))
	return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
	session['name'] = request.form['name']
	return redirect(url_for('ingredients', username=session['name']))

@app.route('/recipe-sets')
def recipe_sets():
	rs = RecipeSet()
	return render_template('recipe-sets.html', recipe_sets=rs.sets)

@app.route('/set/id/<int:set_id>')
def set(set_id):
	recipes = Recipe()
	return render_template('set.html', set= recipes.recipes[set_id])

@app.route('/ingredients/<username>')
def ingredients(username):
	doesExist = UserIngredients.query.filter(UserIngredients.name == username).first()
	if doesExist:
		return 'Ingredients for ' + username
	else: 
		return redirect(url_for('recipe_sets'))
