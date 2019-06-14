# -*- coding: utf-8 -*-`

import Classes
import Functions


SM = Classes.SystemManager()

# Create persons
William = Classes.User("William","Will",23)
Lola = Classes.User("Lola","BabyLola",21)
SM.UserManager.add_user(William)
SM.UserManager.add_user(Lola)

#Create ingredients
PoisChiches = Classes.Ingredient("PoisChiches",300,4.08)
Tahin = Classes.Ingredient("Tahin",30,11.78)
Eau = Classes.Ingredient("Eau Fraiche",100,0)

#Create recipes
RecetteHummusLola = Classes.Recipe("La recette de Hummus de Lola",10,0,Lola)
RecetteHummusLola.add_ingredient(PoisChiches)
RecetteHummusLola.add_ingredient(Tahin)

RecetteHummusWilliam = Classes.Recipe("La recette de Hummus de William",20,0,William)
RecetteHummusWilliam.add_ingredient(PoisChiches)
RecetteHummusWilliam.add_ingredient(Tahin)
RecetteHummusWilliam.display_infos()

RecetteEauFraiche = Classes.Recipe("Une recette d'eau fraîche",0,0,William)
RecetteEauFraiche.add_ingredient(Eau)
RecetteEauFraiche.display_infos()

EauFraiche = Classes.Product("Eau Fraiche")
EauFraiche.add_recipe(SM,EauFraiche)

Hummus = Classes.Product("Hummus")
Hummus.add_recipe(SM,RecetteHummusLola)
Hummus.add_recipe(SM,RecetteHummusWilliam)

SM.ProductManager.add_product(Hummus)
SM.ProductManager.add_product(EauFraiche)

SM.ProductManager.display_product_list()
SM.RecipeManager.display_recipe_list()

#Create product

#Create request


"""
Hummus = Classes.Product("Hummus")
Hummus.add_recipe(RecetteHummus)
Hummus.show_recipes()

RecetteHummus.price_recipe()

print("PRICE OF THE RECIPE:",RecetteHummus.price,"MONECOS")
MyRequest= William.create_request("J'aimerais du Hummus","Hummus",0.5)
RM.add_request(MyRequest)
My2Request= Lola.create_request("J'aimerais des oeufs","Eggs",0.5)
RM.add_request(My2Request)
My3Request= Lola.create_request("J'aimerais du savon","Soap",1)
RM.add_request(My3Request)

RM.remove_request(MyRequest)
"""

