# Innovaccer
# file I/O

import csv

last_names = []
genders = []
dobs = []
first_names = []
n = 0

with open('C:\\Users\\Nikhil\\Downloads\\Deduplication Problem - Sample Dataset.csv','r') as csv_file:
	# here write the location of the data file(here it is Deduplication Problem - Sample Dataset.csv)
	csv_reader = csv.reader(csv_file)

	next(csv_reader)



	for line in csv_reader:
		last_names.append(line[0])
		genders.append(line[2])
		dobs.append(line[1])
		first_names.append(line[3])
		# print(line)
		n = n + 1

	ln=[]
	l_names=[]
	

	for name in last_names:
		for char in name:
			if char==' ':
				break    # here we diffentiated the duplicate last name from the original last name
			ln.append(char)
		ln1=''.join(ln)
		l_names.append(ln1)
		ln=[]
		ln1=''

	# for x in l_names:
	# 	print(x)

	fn=[]
	f_names=[]

	for name in first_names:
		for char in name:
			if char==' ':
				break    # here we diffentiated the duplicate first name from the original first name
			fn.append(char)
		fn1=''.join(fn)
		f_names.append(fn1)
		fn=[]
		fn1=''

	# for x in f_names:
	# 	print(x)

	my_data = [[0 for i in range(4)] for i in range(n)]

	for i in range(n):
		my_data[i][0] = l_names[i]
		my_data[i][1] = dobs[i]
		my_data[i][2] = genders[i]
		my_data[i][3] = f_names[i]

	# print(my_data)



	# we have converted the duplicate entries to identical entries. Now we will load these entries into another file and later we will remove the identical ones
	with open('new_names1.csv','w') as new_file:
		# keep track of this new_names1.csv as we will use this later
		csv_writer = csv.writer(new_file)

		csv_writer.writerows(my_data)








