import csv
input_filename = 'lab1.csv'
output_filename = 'mlab1.csv'
with open(input_filename, 'r', newline='') as infile, open(output_filename, 'w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    header = next(reader)
    writer.writerow(header)
    for row in reader:
        year = row[0]
        modified_date = f"{year}-01-01"
        row[0] = modified_date
        writer.writerow(row)
print(output_filename)
