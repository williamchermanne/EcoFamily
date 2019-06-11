import person,product

William = person.Person("William","Will",23)
Lola=person.Person("Lola","BabyLola",21)
William.displayInfos()
Lola.displayInfos()
person.exchange(Lola,William,10)
William.displayInfos()
Lola.displayInfos()

Hummus = product.Product("Hummus")
Hummus.addIngredient("PoisChiches",4,0.5)
Hummus.addIngredient("Eau",1,1)
Hummus.computeValue(1,10)

Hummus.displayInfos()