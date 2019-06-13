# -*- coding: utf-8 -*-`

import Classes
import Functions
RM = Classes.RequestManager()
William = Classes.Person("William","Will",23, "Pasta")
Lola=Classes.Person("Lola","BabyLola",21, "Hummus")

Hummus = Classes.Ingredient("Hummus",300,4.08)
Tahin = Classes.Ingredient("Tahin",30,11.78)


RecetteHummus = Classes.Recipe("La recette de Hummus de Lola",10,0,Lola)
RecetteHummus.add_ingredient(Hummus)
RecetteHummus.add_ingredient(Tahin)

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
