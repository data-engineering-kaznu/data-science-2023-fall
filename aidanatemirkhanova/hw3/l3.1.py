import csv
data = [
    ['year', 'month', 'region', 'value'],
    ['2022', 'Feb', 'Almaty', '130500'],
    ['2022', 'Feb', 'Astana', '150500'],
    ['2022','Mar', 'Almaty', '150500'],
    ['2022', 'Mar', 'Astana', '150500']
]
filename = 'lab3.csv'
with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    for row in data:
        writer.writerow(row)
with open('lab3.csv', 'r') as file:
    print(file.read())
