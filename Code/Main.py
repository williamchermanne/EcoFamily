# -*- coding: utf-8 -*-`

import Classes
import Functions


SM = Classes.SystemManager()

# Create persons
William = Classes.User(SM,"William","Will",23)
Lola = Classes.User(SM,"Lola","BabyLola",21)
Christine = Classes.User(SM,"Christine","Titine",57)



#Create ingredients
PoisChiches = Classes.Ingredient("PoisChiches",300,4.08)
Tahin = Classes.Ingredient("Tahin",30,11.78)
Eau = Classes.Ingredient("Eau Fraiche",100,0)

#Create recipes
RecetteHummusLola = Classes.Recipe(SM,"La recette de Hummus de Lola",10,0,Lola)
RecetteHummusLola.add_ingredient(PoisChiches)
RecetteHummusLola.add_ingredient(Tahin)

RecetteHummusWilliam = Classes.Recipe(SM,"La recette de Hummus de William",20,0,William)
RecetteHummusWilliam.add_ingredient(PoisChiches)
RecetteHummusWilliam.add_ingredient(Tahin)

RecetteEauFraiche = Classes.Recipe(SM,"Une recette d'eau fraîche",0,0,William)
RecetteEauFraiche.add_ingredient(Eau)


#Create product
EauFraiche = Classes.Product(SM,"Eau Fraiche")
Hummus = Classes.Product(SM,"Hummus")

#Add recipes to product_list

EauFraiche.add_recipe(SM,EauFraiche)
Hummus.add_recipe(SM,RecetteHummusLola)
Hummus.add_recipe(SM,RecetteHummusWilliam)

#Create request
Christine.create_request(SM,"J'aimerais du Hummus",Hummus,1)
Lola.create_request(SM,"Moi aussi!",Hummus,1)
William.create_request(SM,"Moi j'ai soif!",EauFraiche,1)


William.delete_request(SM,3)
Lola.create_request(SM,"Moi j'ai soif soif soif!",EauFraiche,1)

William.accept_request(SM,4)
William.create_rendezvous(SM, 4, "22/07/2019", "00h00", "Charleroi")

Lola.accept_rendezvous(SM,1)
William.display_infos()
Lola.display_infos()

# INFOS
SM.RequestManager.display_request_list()
SM.RendezvousManager.display_rendezvous_list()
William.display_infos()





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
