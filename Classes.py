# Python OOPS

class Employee:

	raise_amt = 1.04

	def __init__(self, first, last, pay):
	 self.first = first
	 self.last = last
	 self.pay = pay
	 self.email = first + '.' + last +'@email.com'

	def fullname(self):
	 return '{} {}'.format(self.first,self.last)

	def apply_raise(self):
	 self.pay = int(self.pay * self.raise_amt)

    @classmethod
	 def set_raise_amt(cls,amount):
		cls.raise_amt = amount

     @classmethod
     def from_string(cls, name):
    	first, last , pay = emp_str.split('-')
    	return cls(first, last, pay)

    @staticmethod
     def is_workday(day):
     	if day.weekday == 5 or day.weekday == 6:
     		return False
     	return True

class Developer(Employee)  #Inheritance
   raise_amt = 1.10

   def __init__(self,first,last,pay,prog_lang):
   	 super() .__init__(first,last,pay)
   	 self.prog_lang = prog_lang

e1 = Employee('Karan','Chauhan','50000','Java')
e2 = Employee('Rahul','Oberoi','60000', 'Scala')

print(e2.email)
print(e1.fullname())
print(Employee.fullname(e2))
print(from_string('vandana-jain-59999'))
