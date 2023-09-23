import csv
with open('HW1_before.csv','r') as input, open('HW1_after.csv','w') as output:
	reader = csv.reader(input)
	writer = csv.writer(output)
	header = next(reader)
	writer.writerow(header)
	for row in reader:
		row[0] +='-01-01'
		writer.writerow(row)
