import csv
data = [
    ['year', 'region', 'value'],
    ['2022-Feb', 'Almaty', '130500'],
    ['2022-Feb', 'Astana', '150500'],
    ['2022-Mar', 'Almaty', '150500'],
    ['2022-Mar', 'Astana', '150500']
]

def transform_date(date_str):
    if date_str == 'year':
        return date_str
    else:
        year, month = date_str.split('-')
        return f'20{year}-{"01" if month == "Jan" else "02" if month == "Feb" else "03"}-01'

for row in data:
    row[0] = transform_date(row[0])

filename = 'tps2.csv'
with open('tps2.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for row in data:
        writer.writerow(row)

