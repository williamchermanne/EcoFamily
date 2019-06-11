class Person:
	def __init__(self, name, pseudo, age):
		self.name = name
		self.pseudo = pseudo
		self.age = age
		self.wallet = 0
	
	def displayInfos(self):
		print(" ")
		print("Name:",self.name)
		print("Pseudo:",self.pseudo)
		print("Age:",self.age)
		print("Wallet:",self.wallet)
		print(" ")
		
	def giveMoney(self,amount):
		self.wallet -=amount
		
	def receiveMoney(self, amount):	
		self.wallet +=amount

		
def exchange(person1,person2,amount):
	print(person1.name,"gives",amount,"to",person2.name)
	person1.giveMoney(amount)
	person2.receiveMoney(amount)
	
	
