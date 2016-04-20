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
                    'image':'/images/broccoli.png'
                },
                {
                    'title': 'Roasted Balsamic Broccoli',
                    'ingredients':[
                        {
                            'name':'frozen (or fresh) broccoli florets',
                            'quantity': '4',
                            'unit':'cups'
                        },
                        {
                            'name':'balsamic vinegar',
                            'quantity': '3',
                            'unit':'tbsps'
                        },
                        {
                            'name':'extra-virgin olive oil',
                            'quantity': '2',
                            'unit':'tbsps'
                        },
                        {
                            'name':'sea salt',
                            'quantity': '1',
                            'unit':'tsp'
                        },
                        {
                            'name':'black pepper',
                            'quantity': '1',
                            'unit':'tsp'
                        },
                        {
                            'name':'garlic salt',
                            'quantity': '1',
                            'unit':'tsp'
                        },
                        {
                            'name':'parmesan cheese (optional)',
                            'quantity': '',
                            'unit':''
                        }
                    ],
                    'steps':[
                        {
                            'text' : 'Preheat oven to 450 degrees.',
                            'number': '1'
                        },
                        {
                            'text' : 'Stir broccoli, balsamic vinegar, olive oil, salt, pepper, and garlic salt in a large bowl until thoroughly combined.',
                            'number': '2'
                        },
                        {
                            'text' : 'Spread broccoli onto a large baking sheet.',
                            'number': '3'
                        },
                        {
                            'text' : 'Roast for 20 minutes or until edges begin to singe and blacken, stirring once on pan halfway through.',
                            'number': '4'
                        },
                        {
                            'text' : 'When broccoli is done transfer to bowl, drizzle with additional balsamic vinegar, and sprinkle with a bit of parmesan cheese if desired.',
                            'number': '5'
                        },
                    ],
                    'image':'/images/balsamic_broccoli.png'
                },
                {
                    'title': 'Clove Garlic Soup',
                    'ingredients':[
                        {
                            'name':'garlic (halved crosswise)',
                            'quantity': '2',
                            'unit':'heads'
                        },
                        {
                            'name':'extra-virgin olive oil',
                            'quantity': '1',
                            'unit':'tbsp'
                        },
                        {
                            'name':'low sodium chicken stock',
                            'quantity': '4',
                            'unit':'cups'
                        },
                        {
                            'name':'yukon gold potatoes',
                            'quantity': '8',
                            'unit':'ozs'
                        },
                        {
                            'name':'freshly grated parmesan',
                            'quantity': '1/4',
                            'unit':'cup'
                        },
                        {
                            'name':'freshly ground pepper',
                            'quantity': '',
                            'unit':''
                        },
                        {
                            'name':'coarse salt',
                            'quantity': '',
                            'unit':''
                        },
                    ],
                    'steps':[
                        {
                            'text' : 'Heat oven to 375 degrees. Drizzle garlic heads with oil. Wrap tightly in foil and roast until tender, about 40 minutes. Let cool, then squeeze garlic from papery skin and set aside.',
                            'number': '1'
                        },
                        {
                            'text' : 'Bring stock, potatoes, and roasted garlic to a boil; reduce heat and simmer until potatoes are tender, about 12 minutes. Remove from heat and stir in Parmesan.',
                            'number': '2'
                        },
                        {
                            'text': 'Let cool slightly, then puree in a blender until smooth. Season with salt and pepper. Sprinkle with Parmesan and serve with rustic bread.',
                            'number': '3'
                        }
                    ],
                    'image':'/images/clove_garlic_soup.png'
                },
                {
                    'title': 'Crockpot BBQ Beef Sandwich',
                    'ingredients':[
                        {
                            'name':'chuck roast',
                            'quantity': '3',
                            'unit':'lbs'
                        },
                        {
                            'name':'seasoning salt',
                            'quantity': '',
                            'unit':''
                        },
                        {
                            'name':'pepper',
                            'quantity': '',
                            'unit':''
                        },
                        {
                            'name':'paprika',
                            'quantity': '',
                            'unit':''
                        },
                        {
                            'name':'garlic powder',
                            'quantity': '',
                            'unit':''
                        },
                        {
                            'name':'bbq sauce',
                            'quantity': '18',
                            'unit':'ozs'
                        },
                        {
                            'name':'beer (stout recommended)',
                            'quantity': '12',
                            'unit':'ozs'
                        }
                    ],
                    'steps':[
                        {
                            'text' : 'Sprinkle both sides of the roast with seasoned salt, pepper, paprika, and garlic powder.',
                            'number': '1'
                        },
                        {
                            'text' : 'Put the roast in your crockpot and pour on the bbq sauce.',
                            'number': '2'
                        },
                        {
                            'text' : 'Pour the beer over the top, and cook for 6-7 hours.',
                            'number': '3.'
                        },
                        {
                            'text' : 'Remove the meat and shred - it should be really tender and falling apart - and discard any fat.',
                            'number': '4'
                        },
                        {
                            'text' : 'Pour the cooking liquid into a large measuring cup and skim off the fat.',
                            'number': '5'
                        },
                        {
                            'text' : 'Mix as much of the liquid back into the meat as you want.',
                            'number': '6'
                        },
                        {
                            'text' : 'Serve immediately, or place beef back in the crockpot on warm until ready to serve.',
                            'number': '7'
                        },
                    ],
                    'image':'/images/crockpot_bbq_beef.png'
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
