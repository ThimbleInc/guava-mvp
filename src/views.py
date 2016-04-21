from flask import render_template, session, request, redirect, url_for
from models.recipe_set import RecipeSet
from models.recipe import Recipe
from models.user_ingredients import UserIngredients
from src import app, db

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
	return render_template('set.html', set=recipes.recipes[set_id], set_id=set_id)

@app.route('/select-set', methods=['POST'])
def add_set():
	set_id = request.form['setID']
	ui = UserIngredients(session['name'], set_id)
	db.session.add(ui)
	db.session.commit()
	return redirect(url_for('ingredients', username=session['name']))

@app.route('/ingredients/<string:username>')
def ingredients(username):
	does_exist = UserIngredients.query.filter(UserIngredients.name == username).first()

	if does_exist:
		set_id = does_exist.recipe_set
		recipe = Recipe()
		recipes = recipe.recipes[set_id]
		return render_template('ingredients.html', recipes=recipes)

	else: 
		return redirect(url_for('recipe_sets'))
