class Ingredient:
    def __init__(self,name,unit,cals):
        self.name = name
        self.unit = unit
        self.cals = cals
    
    def getCals(self):
        return self.cals
    
def calories(ingrs):
    totalcals = 0
    for (amount,ingre) in ingrs:
        if amount == None:
            totalcals = totalcals
        else:
            thiscal = amount * ingre.getCals()
            totalcals = totalcals + thiscal
    return totalcals


frittata_ingredients = [
(3, Ingredient('eggs', '', 60)),
(300, Ingredient('potatoes', 'g', 0.11)),
(1, Ingredient('onions', '', 60)),
(30, Ingredient('grana padano', 'g', 0.4)),
(1, Ingredient('chopped parsley', 'dl', 20)),
(1, Ingredient('olive oil', 'tbsp', 119)),
(1, Ingredient('salt', 'tsp', 0)),
(None, Ingredient('black peppar', '', 0))
]
print(calories(frittata_ingredients))