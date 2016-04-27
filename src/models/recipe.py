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
                    'image':'images/broccoli.png'
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
                    'image':'images/balsamic_broccoli.png'
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
                    'image':'images/clove_garlic_soup.png'
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
                    'image':'images/crockpot_bbq_beef.png'
                }
            ],
            1:[
                {
                    'title': 'Pecan-crusted Chicken',
                    'ingredients':[
                        {
                            'name':'boneless, skinless chicken breast halves',
                            'quantity': '4',
                            'unit':''
                        },
                        {
                            'name':'finely chopped pecans',
                            'quantity': '1/4',
                            'unit':'cup'
                        },
                        {
                            'name':'ground black pepper',
                            'quantity': '1/4',
                            'unit':'tsp'
                        },
                        {
                            'name':'Country Crock pumpkin spice spread',
                            'quantity': '3',
                            'unit':'tbsp'
                        },
                        {
                            'name':'breadcrumbs',
                            'quantity': '1/2',
                            'unit':'cup'
                        }
                    ],
                    'steps':[
                        {
                            'text' : 'Preheat oven to 400 degrees.',
                            'number': '1'
                        },
                        {
                            'text' : 'Combine pecans, bread crumbs and pepper in shallow dish; set aside.',
                            'number': '2'
                        },
                        {
                            'text' : 'Coat chicken with Country Crock Pumpkin Spice Spread, then pecan mixture. Arrange on ungreased baking sheet.',
                            'number': '3'
                        },
                        {
                            'text' : 'Bake 20 minutes or until chicken is thoroughly cooked.',
                            'number': '4'
                        }
                    ],
                    'image':'images/pecan-crusted-chicken.png'
                },
                {
                    'title': 'Sweet Potato Praline',
                    'ingredients':[
                        {
                            'name':'marshmallow creme',
                            'quantity': '1/2',
                            'unit': 'cup'
                        },
                        {
                            'name':'Country Crock pumpkin spice spread',
                            'quantity': '1/4',
                            'unit': 'cup'
                        },
                        {
                            'name':'sweet potatoes, peeled, cooked and mashed',
                            'quantity': '2',
                            'unit': 'lbs'
                        },
                        {
                            'name':'cholesterol-free egg substitute',
                            'quantity': '1/4',
                            'unit': 'cup'
                        },
                        {
                            'name': 'all-purpose flour',
                            'quantity': '2',
                            'unit': 'tbsp'
                        },
                        {
                            'name':'finely chopped pecans',
                            'quantity': '1',
                            'unit':'tbsp'
                        },
                        {
                            'name':'light brown sugar',
                            'quantity': '1',
                            'unit':'tbsp'
                        }
                    ],
                    'steps':[
                        {
                            'text' : 'Beat sweet potatoes, Country Crock Pumpkin Spice Spread, egg substitute and flour in large bowl with electric mixer until fluffy, about 2 minutes.',
                            'number': '1'
                        },
                        {
                            'text' : 'Add marshmallow creme and beat just until blended.',
                            'number': '2'
                        },
                        {
                            'text' : 'Spoon into ungreased 1-1/2-quart casserole.',
                            'number': '3'
                        },
                        {
                            'text' : 'Sprinkle with pecan mixture.',
                            'number': '4'
                        },
                        {
                            'text' : 'Bake 30 minutes or until bubbling.',
                            'number': '5'
                        },
                        {
                            'text' : 'Preheat oven to 350 degrees. Combine pecans with brown sugar in small bowl; set aside.',
                            'number': '6'
                        }
                    ],
                    'image':'images/sweet_potato_praline.png'
                },
                {
                    'title': 'Lemon Chicken with Sweet Potatoes',
                    'ingredients':[
                        {
                            'name': 'sweet potatoes',
                            'quantity': '4',
                            'unit': ''
                        },
                        {
                            'name': 'fresh lemon juice',
                            'quantity': '1/2',
                            'unit': 'cup'
                        },
                        {
                            'name': 'olive oil',
                            'quantity': '1/4',
                            'unit': 'cup'
                        },
                        {
                            'name': 'garlic',
                            'quantity': '2',
                            'unit': 'cloves'
                        },
                        {
                            'name': 'dijon mustard',
                            'quantity': '1',
                            'unit': 'tbsp'
                        },
                        {
                            'name': 'dried oregano',
                            'quantity': '1',
                            'unit': 'tsp'
                        },
                        {
                            'name': 'turmeric',
                            'quantity': '1',
                            'unit': 'tsp'
                        },
                        {
                            'name': 'salt',
                            'quantity': '1/2',
                            'unit': 'tsp'
                        },
                        {
                            'name': 'black pepper',
                            'quantity': '1/2',
                            'unit': 'tsp'
                        },
                        {
                            'name': 'chicken broth',
                            'quantity': '1',
                            'unit': 'cup'
                        },
                        {
                            'name': 'boneless, skinless chicken breasts',
                            'quantity': '2',
                            'unit': ''
                        },
                        {
                            'name': 'lemon',
                            'quantity': '1',
                            'unit': ''
                        }
                    ],
                    'steps':[
                        {
                            'text' : 'Preheat oven to 400 degrees F.',
                            'number': '1'
                        },
                        {
                            'text' : 'Cut sweet potatoes to desired size. Arrange in a deep baking pan.',
                            'number': '2'
                        },
                        {
                            'text' : 'Combine lemon juice, olive oil, garlic, mustard, oregano, turmeric, salt, pepper and chicken broth in a small mixing bowl. Whisk to combine.',
                            'number': '3'
                        },
                        {
                            'text' : 'Place chicken breasts over sweet potatoes and pour lemon mixture on top.',
                            'number': '4'
                        },
                        {
                            'text' : 'Bake 55-60 minutes. If desired, after 30 minutes, arrange lemon slices over chicken and continue baking.',
                            'number': '5'
                        }
                    ],
                    'image':'images/chicken_sweet_potatoes.png'
                },
                {
                    'title': 'Lemon Brownies',
                    'ingredients':[
                        {
                            'name': 'all-purpose flour',
                            'quantity': '1/2',
                            'unit': 'cup'
                        },
                        {
                            'name': 'whole-wheat pastry flour',
                            'quantity': '1/4',
                            'unit': 'cup'
                        },
                        {
                            'name': 'butter',
                            'quantity': '1',
                            'unit': 'stick'
                        },
                        {
                            'name': 'extra large eggs',
                            'quantity': '2',
                            'unit': ''
                        },
                        {
                            'name': 'fresh lemon juice',
                            'quantity': '2',
                            'unit': 'tbsps'
                        },
                        {
                            'name': 'lemon zest',
                            'quantity': '1 1/2',
                            'unit': 'tbsps'
                        },
                        {
                            'name': 'sea salt',
                            'quantity': '1/4',
                            'unit': 'tsp'
                        },
                        {
                            'name': 'baking soda',
                            'quantity': '1/4',
                            'unit': 'tsp'
                        },
                        {
                            'name': 'baking powder',
                            'quantity': '1/4',
                            'unit': 'tsp'
                        },
                        {
                            'name': 'vanilla extract',
                            'quantity': '1/2',
                            'unit': 'tsp'
                        },
                        {
                            'name': 'powdered sugar',
                            'quantity': '1/2',
                            'unit': 'cup'
                        },
                        {
                            'name': 'fresh lemon juice',
                            'quantity': '2',
                            'unit': 'tbsps'
                        },
                        {
                            'name': 'cold water',
                            'quantity': '1/2',
                            'unit': 'tsp'
                        }
                    ],
                    'steps':[
                        {
                            'text' : 'Preheat oven to 340 degrees. Mist a non-stick 8 or 9-inch square pan with cooking spray. Set aside.',
                            'number': '1'
                        },
                        {
                            'text' : 'In a large mixing bowl, beat with a handheld mixer or stand mixer the softened butter with the sugar until fluffy. Add the eggs one at a time until well-incorporated. Add the lemon juice and zest and mix until combined.',
                            'number': '2'
                        },
                        {
                            'text' : 'In a separate bowl, whisk together the flour, salt, baking soda and baking powder. Add the flour mixture into the wet ingredients and beat at medium speed for about 1 to 2 minutes until nice and creamy.',
                            'number': '3'
                        },
                        {
                            'text' : 'Pour batter into prepared pan and bake for about 20-24 minutes. Try not to over-bake. The edges will turn lightly golden brown. A toothpick should have moist crumbs. Let cool on a wire rack for at least 20 minutes.',
                            'number': '4'
                        },
                        {
                            'text' : 'While cooling, prepare the glaze and then spread over the brownies and sprinkle on the zest. Cut into 16 brownies and enjoy!',
                            'number': '5'
                        }
                    ],
                    'image':'images/lemon_brownies.png'
                }
            ],
            2:[
                {
                    'title': 'Quinoa-Stuff Bell Peppers',
                    'ingredients':[],
                    'steps':[],
                    'image':'link/to/image'
                },
                {
                    'title': 'Bell Pepper Eggs',
                    'ingredients':[],
                    'steps':[],
                    'image':'link/to/image'
                },
                {
                    'title': 'Quinoa Stuffing',
                    'ingredients':[],
                    'steps':[],
                    'image':'link/to/image'
                },
                {
                    'title': 'Avocado Egg Chilaquiles',
                    'ingredients':[
                        {
                            'name': 'salsa',
                            'quantity': '1/2',
                            'unit': 'cup'
                        },
                        {
                            'name': '2 large eggs',
                            'quantity': '2',
                            'unit': ''
                        },
                        {
                            'name': 'cilantro (chopped)',
                            'quantity': '1/4',
                            'unit': 'N/A'
                        },
                        {
                            'name': 'Lime',
                            'quantity': '1',
                            'unit': 'N/A'
                        },
                        {
                            'name': 'White corn tortillas',
                            'quantity': '3',
                            'unit': 'N/A'
                        },
                        {
                            'name': 'avocado (diced)',
                            'quantity': '1/2',
                            'unit': 'cup'
                        },
                        {
                            'name': 'purple onion (diced)',
                            'quantity': '2',
                            'unit': 'tbsps'
                        },
                        {
                            'name': 'fresh tomatoes (chopped)',
                            'quantity': '2',
                            'unit': 'tbsps'
                        }
                    ],

                    'steps':[
                        {
                            'text':'Pre-heat oven to 350 degrees. Spread tortilla stirps on baking sheet and bake 10 minutes or until just starting to brown. Cool strips for 10 minutes - they will crisp as they cool.',
                            'number': '1'
                        },
                        {
                            'text' : 'Divide tortilla strips between two individual baking dishes. Top with salsa and place in oven 10 minutes.',
                            'number': '2'
                        },
                        {
                            'text' : 'Toss together avocado, onion tomatoes, cilantro and lime. Set aside.',
                            'number': '3'
                        },
                        {
                            'text' : 'Meanwhile, coat a small skillet with cooking spray. Heat over mediume heat and break eggs into skillet. Cook until desired doneness.',
                            'number': '4'
                        },
                        {
                            'text' : 'Transfer eggs to baking dishes and sprinkle with avocado mixture. Serve with lime wedges.',
                            'number': '5'
                        }
                    ],
                    'image':'link/to/image'
                }
            ]
        }
