class ProductManager:
		ACTIVE_REQUEST = 0
		
		def __init__(self):
			self.request_list=[]
		
		def add_request(self,request):
			self.request_list.append(request)
			
		def remove_request(self,request_id):
			for i in range(len(self.request_list)):
				request = (self.request_list[i])
				if (request.ID == request_id):
					self.request_list.remove(request)
		
		def display_request_list(self):
			for i in range(len(self.request_list)):
				request = (self.request_list[i])
				request.display_infos()


					
			
			
		