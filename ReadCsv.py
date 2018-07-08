import os
import csv

os.chdir('C:/Users/kchauhan/Documents/Sample')

print(os.getcwd())

#with open('name.csv','w') as wf:
	#pass

# with open('name.csv','r') as csv_file:
#    csv_reader = csv.reader(csv_file)
#   # print(csv_reader)
#    #for line in csv_reader:
#    	#print(line)

#    	#print(line[0])

#    with open('new_file.csv', 'w') as new_file:
#    		csv_writer = csv.writer(new_file, delimiter="=")
#    		for line in csv_reader:
#    		 	csv_writer.writerow(line)


 # Dictionary Reader
with open('name.csv','r') as csv_file:
   csv_reader = csv.DictReader(csv_file)

   with open('new_file.csv', 'w') as new_file:
   	fieldnames = ['first_name','last_name']
   	csv_writer = csv.DictWriter(new_file,fieldnames=fieldnames,delimiter="=")
   	for line in csv_reader:
   		del line['email'] # delete email
   		csv_writer.writerow(line)