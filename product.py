class Product:
	def __init__(self, name):
		self.name = name
		self.ListOfIngredients = []
		self.PriceOfIngredients = [] # Prix par kg
		self.QuantityOfIngredients = []	# Quantité en kg
		self.Value = 0
	
	def addIngredient(self,ingredient, price, quantity):
		self.ListOfIngredients.append(ingredient)
		self.PriceOfIngredients.append(price)
		self.QuantityOfIngredients.append(quantity)
	
	def showIngredients(self):
		print("Product:",self.name)
		print("\n")
		for item in range(len(self.ListOfIngredients)):
			print(self.ListOfIngredients[item],"\n","Prix:",self.PriceOfIngredients[item], "€/kg", "Quantity:",self.QuantityOfIngredients[item],"kg")

			
	def computeValue(self,ActiveTime,coefficient):
		IngredientsValue=0
		for item in range(len(self.ListOfIngredients)):
			IngredientsValue += (self.PriceOfIngredients[item])*(self.QuantityOfIngredients[item])
		self.Value= IngredientsValue + coefficient*ActiveTime
		
	def displayInfos(self):
		print(self.name)
		print(self.Value, "EcoEuros")