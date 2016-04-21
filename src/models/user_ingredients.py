from src import db

class UserIngredients(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64), unique=True)
	recipe_set = db.Column(db.Integer)
	recipes_completed = db.Column(db.String(100))
