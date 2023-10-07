import csv
from datetime import datetime
data = [
    ['year','month', 'region', 'value'],
    ['2022','Feb','Almaty','130500'],
    ['2022','Feb','Astana','150500'],
    ['2022','Mar','Almaty','150500'],
    ['2022','Mar','Astana','150500']
]
file_name = "data3.csv"

with open(file_name, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerows(data)
print(f"CSV файл {file_name} успешно создан.")

with open(file_name, 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    read_data = list(csv_reader)

read_data = [list(map(str, row)) for row in read_data]
print(read_data)

for row in data[1:]:
    year_month = row[0] + '-' + datetime.strptime(row[1], '%b').strftime('%m') + "-1"
    del row[0]
    del row[0]
    row.insert(0, year_month)

new_file='output1.csv'
with open(new_file, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerows(data)

print(f"CSV файл {new_file} успешно создан.")

with open(new_file, 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    read_data1 = list(csv_reader)

read_data1 = [list(map(str, row)) for row in read_data1]
print(read_data1)
