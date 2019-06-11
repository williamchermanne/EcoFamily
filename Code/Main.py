import Person,Product,Request

William = Person.Person("William","Will",23)
Lola=Person.Person("Lola","BabyLola",21)


Hummus = Product.Product("Hummus")
Hummus.addIngredient("PoisChiches",4,0.5)
Hummus.addIngredient("Eau",1,1)
Hummus.computeValue(1,10)

Hummus.displayInfos()

William.displayInfos()
Lola.displayInfos()
Person.exchange(Lola,William,Hummus.Value)
William.displayInfos()
Lola.displayInfos()

MyRequest= Request.Request("Hummus",0.5,"Lola")
My2Request= Request.Request("Eggs",0.5,"William")
MyRequest.displayInfos()
My2Request.displayInfos()