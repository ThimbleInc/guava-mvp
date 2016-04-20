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
                    'title': 'Crock Pot Beef & Broccoli',
                    'ingredients':[
                        {
                            'name':'strips of boneless beef chuck roast',
                            'quantity': '1',
                            'unit':'lb'
                        },
                        {
                            'name':'beef consomme',
                            'quantity': '1',
                            'unit':'cup'
                        },
                        {
                            'name':'soy sauce',
                            'quantity': '1/2',
                            'unit':'cup'
                        },
                        {
                            'name':'brown sugar',
                            'quantity': '1/3',
                            'unit':'cup'
                        },
                        {
                            'name':'sesame oil',
                            'quantity': '1',
                            'unit':'tbsp'
                        },
                        {
                            'name':'minced garlic cloves',
                            'quantity': '3',
                            'unit':''
                        },
                        {
                            'name':'corn starch',
                            'quantity': '2',
                            'unit':'tbsps'
                        },
                        {
                            'name':'cooled sauce from the used crock pot',
                            'quantity': '2',
                            'unit':'tbsp'
                        },
                        {
                            'name':'broccoli florets',
                            'quantity': 'as many as desired',
                            'unit':''
                        },
                        {
                            'name':'cooked rice',
                            'quantity': '',
                            'unit':''
                        }
                    ],
                    'steps':[
                        {
                            'text' : 'Place beef in a crock pot.',
                            'number': '1'
                        },
                        {
                            'text' : 'In a small bowl, combine consomme, soy sauce, brown sugar, oil, and garlic. Pour over beef. Cook on low for 6-8 hours.',
                            'number': '2'
                        },
                        {
                            'text' : 'In a cup, stir cornstarch and sauce form the crock pot until smooth. Add to crock pot. Stir well to combine. (If your sauce is not thickening, try bringing your sauce to a boil on the stovetop with the corn starch mixture. Boil until your desired consistency is reached).',
                            'number': '3'
                        },
                        {
                            'text' : 'Add broccoli to the crock pot. Stir to combine.',
                            'number': '4'
                        },
                        {
                            'text' : 'Cover and cook an additional 30 minutes on high (the sauce has to boil for it to thicken).',
                            'number': '5'
                        },
                        {
                            'text' : 'Serve over hot cooked rice.',
                            'number': '6'
                        },
                    ],
                    'image':'link/to/image'
                },
                {
                    'title': 'Roasted Balsamic Broccoli',
                    'ingredients':[
                        {
                            'name':'ing 1',
                            'quantity': '2',
                            'unit':'oz'
                        }
                    ],
                    'steps':[
                        {
                            'text' : 'testy',
                            'number': '1'
                        }
                    ],
                    'image':'link/to/image'
                },
                {
                    'title': 'Clove Garlic Soup',
                    'ingredients':[
                        {
                            'name':'ing 1',
                            'quantity': '2',
                            'unit':'oz'
                        }
                    ],
                    'steps':[
                        {
                            'text' : 'testy',
                            'number': '1'
                        }
                    ],
                    'image':'link/to/image'
                },
                {
                    'title': 'Crockpot BBQ Beef Sandwich',
                    'ingredients':[
                        {
                            'name':'ing 1',
                            'quantity': '2',
                            'unit':'oz'
                        }
                    ],
                    'steps':[
                        {
                            'text' : 'testy',
                            'number': '1'
                        }
                    ],
                    'image':'/images/broccoli.png'
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
