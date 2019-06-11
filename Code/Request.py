class Request:
		requestCount = 0
		
		def __init__(self, product, quantity, addressee):
			self.product=product
			self.quantity=quantity
			self.addressee=addressee
			Request.requestCount+= 1
			self.ID=Request.requestCount
		
		def displayInfos(self):
			print("Request number",self.ID)
			print("Product",self.product)
			print("Addressee",self.addressee)
		