import csv
csv_fileN1 = 'data1.csv'
csv_fileN2 = 'result1.csv'

with open(csv_fileN1, 'r') as csv_file, open(csv_fileN2, 'w', newline='') as csv_file1:
    csv_reader = csv.reader(csv_file)
    csv_write = csv.writer(csv_file1)

    date = []
    for row in csv_reader:
        date.append(row)
    header = date.pop(0)
    for row in date:
        if row[0][:4].isalnum():

                row[0] = row[0][:4] + '-02-01' if row[0][5:] == 'Feb' else row[0][:4] + '-03-01'
    csv_write.writerow(header)
    for row in date:
        csv_write.writerow(row)