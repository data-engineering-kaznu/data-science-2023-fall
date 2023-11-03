import csv
from datetime import datetime

data = [
    ['year', 'region', 'value'],
    ['2022-Feb', 'almaty', 130500],
    ['2022-Feb', 'astana', 150500],
    ['2022-Mar', 'almaty', 150500],
    ['2022-Mar', 'astana', 150500],
    ['2022-Apr', 'astana', 150500]
]
with open('original_data2.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

updated_data = []
with open('original_data2.csv', mode='r') as file:
    reader = csv.reader(file)
    headers = next(reader)
    updated_data.append(headers)

    for row in reader:
        year = row[0]
        date_object = datetime.strptime(year, '%Y-%b')
        row[0] = date_object.strftime('%Y-%m-%d')
        updated_data.append(row)

with open('result_data2.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(updated_data)