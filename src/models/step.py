class Step(object):
    __tablename__ = "step"
    id = Column(Integer, primary_key=True)
    recipe_id = Column(Integer, ForeignKey('recipe.id'))
    number = Column(Integer)
    text = Column(String(300))

    def __init__(self, recipe_id, number, text):
        self.recipe_id = recipe_id
        self.number = number
        self.text = text
