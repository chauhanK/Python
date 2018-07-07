#File Object

#Read File

# r represt read mode, w=write mode, r+=read and write mode
with open('test.txt', 'r') as f:
	print(f.name)
	print(f.mode)
	f_content = f.read()
	print(f_content)

# Read one line at a time
    f_content = f.readline() 
    print(f_content, end='')

     f_content = f.read(100) 
    print(f_content,end='')

    for line in f:
    	print(line,end='')

    size_to_read=10
    f_content = f.read(size_to_read)

#tells the position in file
    f.tell()
 
#starts reading again from the pass position
    f.seek(5)

    while len(f_content) > 0:
       print(f_content,end='==')
        f_content = f.read(size_to_read)


#Write file

with open('test2.txt', 'w') as f:
	#pass #do nothing
	f.write('Test')

	with open('test.txt','r') as rf:
		with open('test_copy.txt', 'w') as wf:
			for line in rf:
				wf.write(line)

# to work with images change the mode from r to rb and w to wb