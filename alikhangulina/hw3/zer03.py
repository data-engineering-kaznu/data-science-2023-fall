import csv
from datetime import datetime

data = [
    ['year', 'month', 'region', 'value'],
    ['2022', 'Feb', 'almaty', '130500'],
    ['2022', 'Feb', 'astana', '150500'],
    ['2022', 'Mar', 'almaty', '150500'],
    ['2022', 'Mar', 'astana', '150500'],
]

with open('original_data3.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

updated_data = []

with open('original_data3.csv', mode='r') as file:
    reader = csv.reader(file)

    for row in reader:
        if row[0] == 'year':
            updated_data.append(['date', 'region', 'value'])
        else:
            year = row[0]
            month = row[1]
            date_string = f'{year}-{month}-01'
            date_object = datetime.strptime(date_string, '%Y-%b-%d')
            formatted_date = date_object.strftime('%Y-%m-%d')
            updated_data.append([formatted_date, row[2], row[3]])

with open('result_data3.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(updated_data)





