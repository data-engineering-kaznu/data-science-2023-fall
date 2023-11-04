import csv

data = [
    ['2022', 'Feb', 'Almaty', '130500'],
    ['2022', 'Feb', 'Astana', '150500'],
    ['2022', 'Mar', 'Almaty', '150500'],
    ['2022', 'Mar', 'Astana', '150500'],
]
with open('hw3.csv', "w") as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    for row in data:
        writer.writerow(row)

def convert_month(month):
    months = {
        'jan': '01',
        'feb': '02',
        'mar': '03',
        'apr': '04',
        'may': '05',
        'jun': '06',
        'jul': '07',
        'aug': '08',
        'sep': '09',
        'oct': '10',
        'nov': '11',
        'dec': '12'
    }
    return months.get(month.lower(), '')

n_data = []
for row in data:
    year = row[0]
    month = convert_month(row[1])
    if month:
        n_date = f"{year}-{month}-01"
        n_row = [n_date, row[2], row[3]]
        n_data.append(n_row)

with open('ozgertilgen.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Data', 'Region', 'Values'])
    csvwriter.writerows(n_data)