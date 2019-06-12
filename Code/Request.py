class Request:
		REQUEST_COUNT = 0
		
		def __init__(self, creator, product, quantity):
			self.creator=creator
			self.product=product
			self.quantity=quantity
			self.status = "pending"
			Request.REQUEST_COUNT+= 1
			self.ID=Request.REQUEST_COUNT
		
		def display_infos(self):
			print("Request number",self.ID)
			print("Product",self.product)
			print("Quantity",self.quantity)
			
		