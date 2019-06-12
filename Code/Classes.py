class Product:
	def __init__(self, name):
		self.name = name
		self.ListOfIngredients = []
		self.PriceOfIngredients = [] # Prix par kg
		self.QuantityOfIngredients = []	# Quantité en kg
		self.Value = 0
	
	def add_ingredient(self,ingredient, price, quantity):
		self.ListOfIngredients.append(ingredient)
		self.PriceOfIngredients.append(price)
		self.QuantityOfIngredients.append(quantity)
	
	def show_ingredients(self):
		print("Product:",self.name)
		print("\n")
		for item in range(len(self.ListOfIngredients)):
			print(self.ListOfIngredients[item],"\n","Prix:",self.PriceOfIngredients[item], "€/kg", "Quantity:",self.QuantityOfIngredients[item],"kg")

			
	def compute_value(self,ActiveTime,coefficient):
		IngredientsValue=0
		for item in range(len(self.ListOfIngredients)):
			IngredientsValue += (self.PriceOfIngredients[item])*(self.QuantityOfIngredients[item])
		self.Value= IngredientsValue + coefficient*ActiveTime
		
	def display_infos(self):
		print(self.name)
		print(self.Value, "Moneco")	
		
		
class Ingredient:
	def __init__(self, name, price, quantity):
		self.name = name
		self.price = price
		self.quantity = quantity
		
class Receipt:
	RECEIPT_COUNT = 0
	def __init__(self):
		Receipt.RECEIPT_COUNT+=1
		self.ID=Receipt.RECEIPT_COUNT

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
	
class Person:
	def __init__(self, name, pseudo, age, specialty):
		self.name = name
		self.pseudo = pseudo
		self.age = age
		self.specialty = specialty
		self.wallet = 0
	
	def display_infos(self):
		print(" ")
		print("Name:",self.name)
		print("Pseudo:",self.pseudo)
		print("Age:",self.age)
		print("Specialty:",self.specialty)
		print("Wallet:",self.wallet)
		print(" ")
		
	def give_money(self,amount):
		self.wallet -=amount
		
	def receive_money(self, amount):	
		self.wallet +=amount
	
	def create_request(self,title,product,quantity):
		request = Request(self.name,title,product,quantity)
		return request


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

				
		
			
	
