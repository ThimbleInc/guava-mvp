class Recipe(object):
    # __tablename__ = "recipe"
    # id = Column(Integer, primary_key=True)
    # title = Column(String(120), unique=True)
    # ingredients = relationship("Ingredient")
    # steps = relationship("Step")
    # image = Column(String(50))
    # recipe_set_id = Column(Integer, ForeignKey('recipe_set.id'))


    # def __init__(self, title, ingredients, steps, recipe_set_id, image):
    #     self.title = title
    #     self ingredients = ingredients
    #     self.steps = steps
    #     self.recipe_set_id = recipe_set_id
    #     self.image = image
    
    def __init__(self):
        self.recipes = {
            0:[
                {
                    'title': 'recipe 1',
                    'ingredients':[
                        {
                            'name':'ing 1',
                            'quantity': '2',
                            'unit':'oz'
                        }
                    ],
                    'steps':[
                        {
                            'text' : 'testy'
                        }
                    ],
                    'image':'link/to/image'
                },
                {
                    'title': 'recipe 2',
                    'ingredients':[
                        {
                            'name':'ing 1',
                            'quantity': '2',
                            'unit':'oz'
                        }
                    ],
                    'steps':[
                        {
                            'text' : 'testy'
                        }
                    ],
                    'image':'link/to/image'
                },
                {
                    'title': 'recipe 3',
                    'ingredients':[
                        {
                            'name':'ing 1',
                            'quantity': '2',
                            'unit':'oz'
                        }
                    ],
                    'steps':[
                        {
                            'text' : 'testy'
                        }
                    ],
                    'image':'link/to/image'
                }
            ],
            1:[
                {
                    'title': 'recipe 1',
                    'ingredients':[],
                    'steps':[],
                    'image':'link/to/image'
                },
                {
                    'title': 'recipe 1',
                    'ingredients':[],
                    'steps':[],
                    'image':'link/to/image'
                },
                {
                    'title': 'recipe 1',
                    'ingredients':[],
                    'steps':[],
                    'image':'link/to/image'
                }
            ],
            2:[
                {
                    'title': 'recipe 1',
                    'ingredients':[],
                    'steps':[],
                    'image':'link/to/image'
                },
                {
                    'title': 'recipe 1',
                    'ingredients':[],
                    'steps':[],
                    'image':'link/to/image'
                },
                {
                    'title': 'recipe 1',
                    'ingredients':[],
                    'steps':[],
                    'image':'link/to/image'
                }
            ],
            3:[
                {
                    'title': 'recipe 1',
                    'ingredients':[],
                    'steps':[],
                    'image':'link/to/image'
                },
                {
                    'title': 'recipe 1',
                    'ingredients':[],
                    'steps':[],
                    'image':'link/to/image'
                },
                {
                    'title': 'recipe 1',
                    'ingredients':[],
                    'steps':[],
                    'image':'link/to/image'
                }
            ]
        }
