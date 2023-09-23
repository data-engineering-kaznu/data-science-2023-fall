import csv

data = [['year', 'region', 'value'],
        ['2020','Almaty', '130500'],
        ['2021','Almaty', '150500']]

with open('data.csv', 'w') as f:
    writer = csv.writer(f)
    for row in data:
        writer.writerow(row)

with open('data.csv') as f:
    print(f.read())

with open('data.csv', 'w') as f2:
    writer = csv.writer(f2)
    writer.writerow(data[0])
    data.pop(0)
    for row in data:
        row[0] += "-01-01"
        writer.writerow(row)

with open('data.csv') as f:
    print(f.read())

