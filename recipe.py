def adapt_recipe(txt, x):
    new_recipe = ""
    allrows = txt.split('\n')
    for row in allrows:
        for word in row.split():
            if word.isdigit():
                new_recipe = new_recipe + str((int(word) * x))
            else:
                new_recipe = new_recipe + word
            new_recipe = new_recipe + " "
        new_recipe = new_recipe + '\n'
    return new_recipe









frittata = """3 eggs
300 g potatoes
1 onion
30 g grana padano
1 dl chopped parsley
2 tbsp olive oil
1 tsp salt
black pepper
"""
print(adapt_recipe(frittata,0.5))