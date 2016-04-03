class RecipeSet(Base):
    __tablename__ = "recipe_set"
    id = Column(Integer, primary_key=True)
    recipes = relationship("Recipe")
    description = Column(String(300))
    feature_image = Column(String(50))

    def __init__(self, recipes, description, feature_image):
        self.recipes = recipes
        self.description = description
        self.feature_image = feature_image
        