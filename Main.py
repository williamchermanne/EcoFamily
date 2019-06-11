import person

William = person.Person("William","Will",23,0)
Lola=person.Person("Lola","BabyLola",21,0)
William.displayInfos()
Lola.displayInfos()
person.exchange(Lola,William,10)
William.displayInfos()
Lola.displayInfos()
