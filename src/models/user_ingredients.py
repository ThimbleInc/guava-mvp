from src import db

class UserIngredients(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), unique=True)
	recipe_set = db.Column(db.Integer)
	recipes_completed = db.Column(db.String(100))

	def __init__(self, name, recipe_set):
		self.name = name
		self.recipe_set = recipe_set