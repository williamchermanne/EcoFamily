import Classes

RM = Classes.RequestManager()
William = Classes.Person("William","Will",23, "Pasta")
Lola=Classes.Person("Lola","BabyLola",21, "Hummus")

Hummus = Classes.Ingredient("Hummus",1,0.1)
Eau = Classes.Ingredient("Eau",0.5,0)


RecetteHummus = Classes.Recipe("La recette de Hummus de Lola",Lola)
RecetteHummus.add_ingredient(Hummus)
RecetteHummus.add_ingredient(Eau)
RecetteHummus.display_infos()

Hummus = Classes.Product("Hummus")
Hummus.add_recipe(RecetteHummus)
Hummus.show_recipes()


MyRequest= William.create_request("J'aimerais du Hummus","Hummus",0.5)
RM.add_request(MyRequest)
My2Request= Lola.create_request("J'aimerais des oeufs","Eggs",0.5)
RM.add_request(My2Request)
My3Request= Lola.create_request("J'aimerais du savon","Soap",1)
RM.add_request(My3Request)

RM.remove_request(MyRequest)
