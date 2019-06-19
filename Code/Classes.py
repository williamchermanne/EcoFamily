# -*- coding: utf-8 -*-`

import Functions

class Ingredient:
	def __init__(self, name, quantity, price):#quantity is in grams
		self.name = name
		self.price = price #price per kg
		self.quantity = (quantity/1000) #in kg

	def display_infos(self):
		print("Name:",self.name)
		print("Quantity:",self.quantity,"kg or L")
		print("Price:",self.price,"euros/kg")
		print(" ")


class Recipe:
	RECIPE_COUNT = 0
	def __init__(self, SystemManager, name, active_time, passive_time, creator):
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

		SystemManager.RecipeManager.add_recipe(self)

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
		print ("Recipe from",self.creator.name)
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
		self.recipe_list.remove(recipe)
		RecipeManager.number_of_recipes -= 1

	def display_recipe_list(self):
		print("Recipe list:")
		for recipe in self.recipe_list:
			print(recipe.name)

class Product:
	def __init__(self, SystemManager, name):
		self.name = name
		self.recipe_list = []
		SystemManager.ProductManager.add_product(self)

	def add_recipe(self,SystemManager,recipe):
		self.recipe_list.append(recipe)


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
		print(" ")
		print("Product list:")
		print(" ")
		for product in self.product_list:
			product.display_infos()

class Request:
	REQUEST_COUNT = 0

	def __init__(self, SystemManager, creator, name, product, quantity):
		self.name = name
		self.creator = creator
		self.acceptor = None
		self.product=product
		self.quantity=quantity
		self.status = "pending" # Can be either pending, accepted or done
		Request.REQUEST_COUNT+= 1
		self.ID=Request.REQUEST_COUNT

		SystemManager.RequestManager.add_request(self)

	def display_infos(self):
		print("Request number",self.ID,"from",self.creator, ":",self.name,"(Status =",self.status,")")
		print("Product:",self.product.name)
		print("Quantity:",self.quantity,"kg or L")
		print("Status:",self.status)
		if (self.status == "accepted"):
			print("Acceptor:",self.acceptor.name)


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

	def update(self):
		for request in self.request_list:
			if (request.status == "accepted"):
				self.request_list.remove(request)

	def display_request_list(self):
		print(" ")
		print("Request list:")
		print(" ")
		for request in self.request_list:
			request.display_infos()


class User:
	USER_COUNT = 0
	def __init__(self, SystemManager, name, pseudo, age):
		self.name = name
		self.pseudo = pseudo
		self.age = age
		self.specialty = ""
		self.wallet = 0
		self.request_accepted_list = []
		self.request_sent_list = []
		self.rendezvous_list = []
		User.USER_COUNT+= 1
		self.ID=User.USER_COUNT

		SystemManager.UserManager.add_user(self)

	def give_money(self,amount):
		self.wallet -= amount

	def receive_money(self, amount):
		self.wallet += amount

	def create_request(self,SystemManager,name,product,quantity):
		request = Request(SystemManager,self,name,product,quantity)
		self.request_sent_list.append(request)

	def delete_request(self, SystemManager, requestID):
		for request in self.request_sent_list:
			if (request.ID == requestID):
				self.request_sent_list.remove(request)
				SystemManager.RequestManager.remove_request(request)

	def accept_request(self,SystemManager,requestID):
		for request in SystemManager.RequestManager.request_list:
			if (request.ID == requestID):
				request.status = "accepted"
				request.acceptor = self
				self.request_accepted_list.append(request)

	def create_rendezvous(self,SystemManager,requestID,date,time,location):
		for request in self.request_accepted_list:
			if (request.ID == requestID):
				myrequest = request
				rendezvous = Rendezvous(SystemManager,self,myrequest.creator,myrequest,date,time,location)
				print(rendezvous.creator.name)
				print(myrequest.creator)
				self.rendezvous_list.append(rendezvous)

	def accept_rendezvous(self, SystemManager, rendezvousID):
		for rendezvous in SystemManager.RendezvousManager.rendezvous_list:
			if (rendezvous.destinator == self):
				self.rendezvous_list.append(rendezvous)
				rendezvous.status = "accepted"

	def delete_rendezvous(self, SystemManager, rendezvousID):
		for rendezvous in self.rendezvous_list:
			if (rendezvous.ID == rendezvousID):
				self.rendezvous_list.remove(rendezvous)
				SystemManager.RendezvousManager.remove_rendezvous(rendezvous)

	def display_infos(self):
		print(" ")
		print("Name:",self.name)
		print("Pseudo:",self.pseudo)
		print("Age:",self.age)
		print("Specialty:",self.specialty)
		print("Wallet:",self.wallet)
		print("Active rendezvous:")
		for rendezvous in self.rendezvous_list:
			rendezvous.display_infos()
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
		print(" ")
		print("User list:")
		print(" ")
		for user in self.user_list:
			print(user.name)

class Rendezvous:
	RENDEZVOUS_COUNT = 0

	def __init__(self,SystemManager, creator,destinator,request,date,time,location):
		self.status = "pending"
		self.creator = creator
		self.destinator = destinator
		self.date = date
		self.time = time
		self.location = location
		self.request = request
		Rendezvous.RENDEZVOUS_COUNT+= 1
		self.ID=Rendezvous.RENDEZVOUS_COUNT

		SystemManager.RendezvousManager.add_rendezvous(self)

	def display_infos(self):
		print("Rendezvous number",self.ID,"between",self.creator.name,"and",self.destinator.name, "(Status =",self.status,")")
		print("Date",self.date)
		print("Time",self.time)
		print("Location",self.location)

class RendezvousManager:
	number_of_rendezvous = 0

	def __init__(self):
		self.rendezvous_list=[]

	def add_rendezvous(self,rendezvous):
		self.rendezvous_list.append(rendezvous)
		RendezvousManager.number_of_rendezvous += 1

	def remove_rendezvous(self,rendezvous):
		self.rendezvous_list.remove(rendezvous)
		RendezvousManager.number_of_rendezvous-= 1

	def update(self):
		for rendezvous in self.rendezvous_list:
			if (rendezvous.status == "done"):
				self.rendezvous_list.remove(rendezvous)
	def display_rendezvous_list(self):
		print(" ")
		print("Rendezvous list:")
		print(" ")
		for rendezvous in self.rendezvous_list:
			rendezvous.display_infos()

class SystemManager:

	def __init__(self):
		self.UserManager = UserManager()
		self.RequestManager = RequestManager()
		self.RecipeManager = RecipeManager()
		self.ProductManager = ProductManager()
		self.RendezvousManager = RendezvousManager()
