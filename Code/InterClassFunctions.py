def RecipePrice(myRecipe):
    priceTot = 0
    for ingredient in myRecipe.ingredient_list:
        priceTot = priceTot + ingredient.price*ingredient.quantity
    return priceTot
