file = open('test.txt','w')
file.write('Hello!\n')
file.write('My name is Py\n')
file.close()
with open('test.txt','r') as f:
	for line in f:
		print(line.strip())