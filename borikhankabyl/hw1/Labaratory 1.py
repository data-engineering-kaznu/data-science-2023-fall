import csv

data = [
    ['year', 'region', 'value'],
    ['2020', 'Almaty', '130500'],
    ['2021', 'Almaty', '135000'],
    ['2022', 'Almaty', '140000'],
]

filename = 'Lab.csv'

with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
   
    for row in data:
        writer.writerow(row)



# Изменение данных 
new_value = '2020-01-01'
data[1][0] = new_value

with open('Lab.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

with open('Lab.csv', 'r') as file:
    print(file.read())
