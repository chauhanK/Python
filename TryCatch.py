
try:
	f=open('testfile.txt')

except FileNotFoundError as e:
   print(e)

else:
	print(f.read())
	f.close()

finally:
	print("Exceuting Finally.....")

