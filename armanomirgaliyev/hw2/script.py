import csv

csv_file_path = 'original.csv'
csv_file_write = 'result.csv'

with open(csv_file_path, 'r') as csv_file, open(csv_file_write, 'w', newline='') as csv_file1:
    csv_reader = csv.reader(csv_file)
    csv_write = csv.writer(csv_file1)

    date = []
    for row in csv_reader:
        date.append(row)

    for row in date:
        if row[0][:4].isalnum():
            if row[0][5:] == 'Feb':
                row[0] = row[0][:4] + '-02-01'
            elif row[0][5:] == 'Jan':
                row[0] = row[0][:4] + '-01-01'
            elif row[0][5:] == 'Jun':
                row[0] = row[0][:4] + '-06-01'
            else: row[0] = row[0][:4] + '-03-01'

    for row in date:
        csv_write.writerow(row)
    
