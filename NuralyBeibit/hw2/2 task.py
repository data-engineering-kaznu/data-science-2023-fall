import csv
csv_fileN1 = 'number.csv'
csv_fileN2 = 'number2.csv'

with open(csv_fileN1, 'r') as csv_file, open(csv_fileN2, 'w', newline='') as csv_file1:
    csv_reader = csv.reader(csv_file)
    csv_write = csv.writer(csv_file1)

    date = []
    for row in csv_reader:
        date.append(row)

    for row in date:

    for row in date:
        if row[0][:4].isalnum():
            if row[0][5:] == 'Feb':
                row[0] = row[0][:4] + '-02-01'
            else:
                row[0] = row[0][:4] + '-03-01'

    for row in date:
        csv_write.writerow(row)