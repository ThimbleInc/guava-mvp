from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'homepage'

@app.route('/recipe-sets')
def recipe_sets():
	return 'recipe sets'

@app.route('/set/id/<int:set_id>')
def set(set_id):
	return 'Set ID is ' + str(set_id)

@app.route('/ingredients/<username>')
def ingredients(username):
	return 'Ingredients for ' + username

if __name__ == '__main__':
    app.run(debug=True)