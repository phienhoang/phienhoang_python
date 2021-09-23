import csv
with open('table.csv','r') as f:
	csv_reader = csv.reader(f, delimiter=';')
	reader = []
	for line in csv_reader:
		reader.append(line)

new = [5]*len(reader[0])
reader.insert(2,new)
with open('middle_row.csv','w') as new_file:
	csv_writer = csv.writer(new_file, delimiter=',')
	for line in reader:
		csv_writer.writerow(line)