# Python OOPS

class Employee:

	def __init__(self, first, last, pay):
	 self.first = first
	 self.last = last
	 self.pay = pay
	 self.email = first + '.' + last +'@email.com'

e1 = Employee('Karan','Chauhan','50000')
e2 = Employee('Rahul','Oberoi','60000')

print(e2.email)

