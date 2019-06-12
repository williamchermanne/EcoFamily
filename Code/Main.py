# -*- coding: utf-8 -*-`

import Classes

RM = Classes.RequestManager()
William = Classes.Person("William","Will",23, "Pasta")
Lola=Classes.Person("Lola","BabyLola",21, "Hummus")

Hummus = Classes.Product("Hummus")
Hummus.add_ingredient("PoisChiches",4,0.5)
Hummus.add_ingredient("Eau",1,1)
Hummus.compute_value(1,10)

MyRequest= William.create_request("J'aimerais du Hummus","Hummus",0.5)
RM.add_request(MyRequest)
My2Request= Lola.create_request("J'aimerais des oeufs","Eggs",0.5)
RM.add_request(My2Request)
My3Request= Lola.create_request("J'aimerais du savon","Soap",1)
RM.add_request(My3Request)

RM.remove_request(MyRequest)
