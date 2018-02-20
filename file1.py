import csv

with open('H:\\Sublime Text 3\\new_names1.csv','r') as infile, open('output.csv','w') as outfile:
	# here write the location of the output file(new_names1.csv) obtained from previous code
	seen = set()
	lt = ["last name","DOB","gender","first name"]
	writer = csv.writer(outfile)
	writer.writerow(lt)
	for line in infile:
		if line in seen:
			continue    # duplicate ones are eliminated
		seen.add(line)
		outfile.write(line)