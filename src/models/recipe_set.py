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
				'title' : 'recipe set 1',
				'description' : 'succulent recipe set 1',
				'link' : '/set/id/0',
				'feature_image' : '/blah.png',
				'set_id' : 0
			},
			{
				'title' : 'recipe set 2',
				'description' : 'succulent recipe set 2',
				'link' : '/set/id/1',
				'feature_image' : '/blah.png',
				'set_id' : 1

			},
			{
				'title' : 'recipe set 3',
				'description' : 'succulent recipe set 3',
				'link' : '/set/id/2',
				'feature_image' : '/blah.png',
				'set_id' : 2

			},
			{
				'title' : 'recipe set 4',
				'description' : 'succulent recipe set 4',
				'link' : '/set/id/3',
				'feature_image' : '/blah.png',
				'set_id' : 3
			},
		]

