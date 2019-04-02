#Airline / Hotel Reservation System - Create a reservation system which books airline seats .
# It charges various rates for particular sections of the plane or hotel. Example, first class is going to cost more than coach. 

class BoardingPass(object):
	baseprice=3000

	def __init__(self, date, from_destination, to_destination, no_of_Passengers,baseprice=3000):
		self.date = date
		self.from_destination = from_destination
		self.to_destination = to_destination
		self.no_of_Passengers = no_of_Passengers
		self.baseprice = baseprice
		self.price = no_of_Passengers * baseprice
	
	def economy_class(self):
		print("expected price: ",self.price )
		return self.price

	def buisness_class(self):
		self.price *= 2
		print("expected price: ",self.price )
		return self.price
	
	def first_class(self):
		self.price *= 4
		print("expected price: ",self.price )
		return self.price
	

a=str(input("enter the date: "))
b=input("enter from destination: ")
c=input("enter to destination: ")
d=eval(input("enter the number of passengers: "))
available_class= {1:"Economyclass", 2:"Buisnessclass", 3:"firstclass"}


for k,v in available_class.items():
	print(k,v) 
e=int(input("enter the required_class: "))
m = BoardingPass(a,b,c,d)
if e == 1:
	print(m.economy_class())
elif e == 2:
	print(m.buisness_class())
elif e == 3:
	print(m.first_class())
else:
	print("invalid operation")




		


