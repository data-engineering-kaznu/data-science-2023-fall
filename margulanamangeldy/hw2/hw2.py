import csv

st = [['year', 'region', 'value'],
      ['2020-Feb', 'Almaty', '130500'],
      ['2020-Feb', 'Astana', '150500'],
      ['2020-Mar', 'Almaty', '150500'],
      ['2020-Mar', 'Astana', '150500']]


with open('file_data.csv', 'w', newline='') as csv_output:
    w = csv.writer(csv_output)
    w.writerows(st)


with open('file_data.csv', 'r', newline='') as csv_input:
    rows = list(csv.reader(csv_input))


for row in rows:
    if row[0] == '2020-Feb':
        row[0] = '2020-02-01'
    elif row[0] == '2020-Mar':
        row[0] = '2020-03-01'

with open('file_result.csv', 'w', newline='') as csv_output:
    w = csv.writer(csv_output)
    w.writerows(rows)
