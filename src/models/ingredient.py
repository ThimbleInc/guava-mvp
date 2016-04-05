class Ingredient(object):
    __tablename__ = "ingredient"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    quantity = Column(Float)
    unit = Column(String(20))
    recipe_id = Column(Integer, ForeignKey('recipe.id'))

    def __init__(self, name, quantity, unit, recipe_id):
        self.name = name
        self.quantity = quantity
        self.unit = unit
        self.recipe_id = recipe_id
        

ingredients = {}
