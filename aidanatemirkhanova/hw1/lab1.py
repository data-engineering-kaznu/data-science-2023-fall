import csv

data = [
    ['year', 'region', 'value'],
    ['2020', 'Almaty', '130500'],
    ['2021', 'Almaty', '150500']
]

filename = 'lab1.csv'

with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
   
    for row in data:
        writer.writerow(row)

with open('lab1.csv', 'r') as file:
    print(file.read())
