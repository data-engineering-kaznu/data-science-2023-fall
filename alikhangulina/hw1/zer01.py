import csv

data = [
    ['year', 'region', 'value'],
    [2020, 'almaty', 130500],
    [2021, 'almaty', 150500]
]
with open('original_data1.csv', mode='w') as file:
    writer = csv.writer(file)
    writer.writerows(data)

updated_data = []
with open('original_data1.csv', mode='r') as file:
    reader = csv.reader(file)
    headers = next(reader)
    updated_data.append(headers)

    for row in reader:
        year = row[0]
        if year == '2020':
            row[0] = '2020-01-01'
        if year == '2021':
            row[0] = '2021-01-01'
        updated_data.append(row)

with open('result_data1.csv', mode='w') as file:
    writer = csv.writer(file)
    writer.writerows(updated_data)

