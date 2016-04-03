class Recipe(Base):
    __tablename__ = "recipe"
    id = Column(Integer, primary_key=True)
    title = Column(String(120), unique=True)
    ingredients = relationship("Ingredient")
    steps = relationship("Step")
    image = Column(String(50))
    recipe_set_id = Column(Integer, ForeignKey('recipe_set.id'))


    def __init__(self, title, ingredients, steps, recipe_set_id, image):
        self.title = title
        self ingredients = ingredients
        self.steps = steps
        self.recipe_set_id = recipe_set_id
        self.image = image
