def define_moneco():
# This function defines the current status of the moneco value. 
# A price is computed as is : Price_moneco = a*price_euros + b* active_time + c*passive_time
	a = 1 #monecos per euros
	b= 1/60 #monecos per minute
	c= (0.5)/60 #monecos per minute
	parameters = [a,b,c]
	return parameters
	
def compute_price(investment,active_time,passive_time):
	parameters = define_moneco()
	total_price = investment*parameters[0] + active_time*parameters[1] + passive_time**parameters[2]
	total_price = round(total_price,2)
	return total_price