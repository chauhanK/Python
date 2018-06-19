#no need of semi colon and datatype
message = "Hello World"                               

print(message)

#muliple line 
my_message = """Hello, Welcome to Python's World      
You gonna love it"""                                   

print(my_message)

#length of a string
print(len(message))                                   

#print 6th character of a string
print(message[6])                                   

#first index is inclusive and last index is exclusive.... prints character from 0 to 4
print(message[0:5])                                   

#if starting from 0 first index is not necessary
print(message[:5]) 

#print chars from 6 to 10                              
print(message[6:11])                                 

#if ending at last charcter of string,then last index is not necessary
print(message[6:])

print(message.lower()) 

print(message.upper())

print(message.count('l'))

print(message.find('World'))

message = message.replace('World', 'Universe')

print(message)

#concat
greeting = "Hello"
name = "Karan"

#Concat using + operator
message = greeting + ', ' + name + '.' + 'Welcome!'

#Concat using String format
message = '{}, {}. Welcome!'.format(greeting,name)

#Concat using f string
message = f'{greeting}, {name.upper()}.Welcome!'

print(message)

