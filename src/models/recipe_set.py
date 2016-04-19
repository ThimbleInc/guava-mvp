class RecipeSet(object):
    # __tablename__ = "recipe_set"
    # id = Column(Integer, primary_key=True)
    # recipes = relationship("Recipe")
    # description = Column(String(300))
    # feature_image = Column(String(50))
    # link = Column(String(50))

    # def __init__(self, recipes, description, feature_image, link):
    #     self.recipes = recipes
    #     self.description = description
    #     self.feature_image = feature_image
    #     self.link = link
    
   	def __init__(self):
   		self.sets = [
			{
				'title' : 'Hearty Meals',
				'description' : 'These four dishes provide that warm feeling inside your tummy. The main themes of this recipe set \
				include slow cooking, meaty and BROCCOLI!',
				'link' : '/set/id/0',
				'feature_image' : '/blah.png',
				'set_id' : 0
			},
			{
				'title' : 'Sweet and Savory',
				'description' : 'This meal set provides the best of two worlds, sweet and savory! Enjoy two scrumptious \
				chicken meals, and two sweet dishes for your sweet tooth.',
				'link' : '/set/id/1',
				'feature_image' : '/blah.png',
				'set_id' : 1

			},
			{
				'title' : 'Veggie Delight',
				'description' : 'Four delicious meals made just for the vegetarian in you. The base ingredients for this set are \
				bell peppers, eggs, and quinoa.',
				'link' : '/set/id/2',
				'feature_image' : '/blah.png',
				'set_id' : 2

			},
		]

