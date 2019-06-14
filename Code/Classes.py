import Functions
		
class Ingredient:
	def __init__(self, name, quantity, price):#quantity is in grams
		self.name = name
		self.price = price #price per kg
		self.quantity = (quantity/1000) #in kg
		
	def display_infos(self):
		print("Name:",self.name)
		print("Quantity:",self.quantity,"kg or L")
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
		ingredient_counter = 0
		Recipe.price_recipe(self)
		print(self.name)
		print("Recipe from",self.creator.name)
		print("Price:",self.price)
		print("Active time:",self.active_time,"min")
		print("Passive time:",self.passive_time,"min")
		for ingredient in self.ingredient_list:
			ingredient_counter += 1
			print("Ingredient number",ingredient_counter)
			ingredient.display_infos()
		print(self.comment)
	
class RecipeManager:
	number_of_recipes = 0
		
	def __init__(self):
		self.recipe_list=[]
		
	def add_recipe(self,recipe):
		self.recipe_list.append(recipe)
		RecipeManager.number_of_recipes += 1
		
	def remove_request(self,recipe):
		self.recipe_list.remove(request)
		RecipeManager.number_of_recipes -= 1
		
	def display_recipe_list(self):
		print("Recipe list:")
		for recipe in self.recipe_list:
			print(recipe.name)	

class Product:
	def __init__(self, name):
		self.name = name
		self.recipe_list = []
	
	def add_recipe(self,SystemManager,recipe):
		self.recipe_list.append(recipe)
		SystemManager.RecipeManager.add_recipe(recipe)

	def remove_recipe(self,recipe):
		self.recipe_list.remove(recipe)
	
	def display_infos(self):
		print("Product:",self.name)
		print("Recipes:")
		for recipe in self.recipe_list:
			print(recipe.name)
			
class ProductManager:
	number_of_products = 0
		
	def __init__(self):
		self.product_list=[]
		
	def add_product(self,product):
		self.product_list.append(product)
		ProductManager.number_of_products += 1
			
	def remove_product(self,product):
		self.product_list.remove(product)
		ProductManager.number_of_products -= 1
		
	def display_product_list(self):
		print("Product list:")
		for product in self.product_list:
			product.display_infos()			
		
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
	number_of_requests = 0
		
	def __init__(self):
		self.request_list=[]
		
	def add_request(self,request):
		self.request_list.append(request)
		RequestManager.number_of_requests += 1
			
	def remove_request(self,request):
		self.request_list.remove(request)
		RequestManager.number_of_requests -= 1
		
	def display_request_list(self):
		print("Rquest list:")
		for request in self.request_list:
			request.display_infos()

class User:
	USER_COUNT = 0
	def __init__(self, name, pseudo, age):
		self.name = name
		self.pseudo = pseudo
		self.age = age
		self.specialty = ""
		self.wallet = 0
		User.USER_COUNT+= 1
		self.ID=User.USER_COUNT
		
	def give_money(self,amount):
		self.wallet -= amount
		
	def receive_money(self, amount):	
		self.wallet += amount
	
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

class UserManager:
	number_of_users = 0
	
	def __init__(self):
		self.user_list=[]
		
	def add_user(self,user):
		self.user_list.append(user)
		UserManager.number_of_users += 1
			
	def remove_user(self,user):
		self.user_list.remove(user)
		UserManager.number_of_users -= 1
		
	def display_user_list(self):
		print("User list:")
		for user in self.user_list:
			print(user.name)
			
class SystemManager:

	def __init__(self):
		self.UserManager = UserManager()
		self.RequestManager = RequestManager()
		self.RecipeManager = RecipeManager()
		self.ProductManager = ProductManager()
	
		
			
	
