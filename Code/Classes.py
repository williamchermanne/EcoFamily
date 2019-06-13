import Functions
		
class Ingredient:
	def __init__(self, name, quantity, price):#quantity is in grams
		self.name = name
		self.price = price #price per kg
		self.quantity = (quantity/1000) #in kg
		
	def display_infos(self):
		print("Name:",self.name)
		print("Quantity:",self.quantity,"kg")
		print("Price:",self.price,"€/kg")
		print(" ")
		

class Recipe:
	RECIPE_COUNT = 0
	def __init__(self, name,active_time,passive_time,creator):
		Recipe.RECIPE_COUNT+=1
		self.ID=Recipe.RECIPE_COUNT
		self.ingredient_list=[]
		self.ingredients_price=0 #in euros
		self.name = name
		self.creator = creator
		self.comment = ""
		self.active_time = active_time #in minutes
		self.passive_time = passive_time #in minutes
		self.price = 0
	
	def add_comment(self,comment):
		self.comment = comment
		
	def add_ingredient(self,ingredient):
		self.ingredient_list.append(ingredient)
	
	def remove_ingredient(self, ingredient):
		self.ingredient_list.remove(ingredient)
		
	def price_recipe(self):
		ingredients_price = 0
		for ingredient in self.ingredient_list:
			ingredients_price = ingredients_price + ingredient.price*ingredient.quantity
		self.ingredients_price = ingredients_price
		self.price = Functions.compute_price(ingredients_price,self.active_time,self.passive_time)
	
	def display_infos(self):
		print("")
		print("Recipe from",self.creator.name, ":")
		for i in range(len(self.ingredient_list)):
			ingredient = (self.ingredient_list[i])
			print("Ingredient number",i+1)
			ingredient.display_infos()
		print(self.comment)
	
	

class Product:
	def __init__(self, name):
		self.name = name
		self.recipe_list = []
		self.selected_recipe = None 
		self.value = 0
	
	def add_recipe(self,recipe):
		self.recipe_list.append(recipe)
		
	def remove_recipe(self,recipe):
		self.recipe_list.remove(recipe)
	
	def show_recipes(self):
		print("Product:",self.name)
		for i in range(len(self.recipe_list)):
			recipe = (self.recipe_list[i])
			print("Recipe number",recipe.ID)
			recipe.display_infos()
		
	def display_infos(self):
		print(self.name)
		print(self.Value, "Moneco")	
		
class Request:
	REQUEST_COUNT = 0
		
	def __init__(self, title, creator, product, quantity):
		self.title= title
		self.creator=creator
		self.product=product
		self.quantity=quantity
		self.status = "pending"
		Request.REQUEST_COUNT+= 1
		self.ID=Request.REQUEST_COUNT
		
	def display_infos(self):
		print("Request number",self.ID,"from",self.creator)
		print("Product",self.product)
		print("Quantity",self.quantity)
	
class RequestManager:
	ACTIVE_REQUEST = 0
		
	def __init__(self):
		self.request_list=[]
		
	def add_request(self,request):
		self.request_list.append(request)
			
	def remove_request(self,request):
		self.request_list.remove(request)
		
	def display_request_list(self):
		for i in range(len(self.request_list)):
			request = (self.request_list[i])
			request.display_infos()

class Person:
	def __init__(self, name, pseudo, age, specialty):
		self.name = name
		self.pseudo = pseudo
		self.age = age
		self.specialty = specialty
		self.wallet = 0
		
	def give_money(self,amount):
		self.wallet -=amount
		
	def receive_money(self, amount):	
		self.wallet +=amount
	
	def create_request(self,title,product,quantity):
		request = Request(self.name,title,product,quantity)
		return request	

	def display_infos(self):
		print(" ")
		print("Name:",self.name)
		print("Pseudo:",self.pseudo)
		print("Age:",self.age)
		print("Specialty:",self.specialty)
		print("Wallet:",self.wallet)
		print(" ")
						
		
			
	
