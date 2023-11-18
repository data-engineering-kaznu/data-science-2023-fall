import csv

with open('ht-result.csv', "w", newline='', encoding='utf-8') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerow(['year', 'region', 'value'])
    writer.writerow(['2020-01-01', 'Almaty', 130500])
    writer.writerow(['2021-01-01', 'Almaty', 150500])

with open('ht-result.csv', newline='', encoding='utf-8') as f:
    re = csv.reader(f)
    for row in re:
       print(row)