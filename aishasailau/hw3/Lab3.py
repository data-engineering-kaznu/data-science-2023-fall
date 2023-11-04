import csv

data = [
    ["year", "month", "region", "value"],
    ["2022", "Feb", "Almaty", "130500"],
    ["2022", "Feb", "Astana", "150500"],
    ["2022", "Mar", "Almaty", "150500"],
    ["2022", "Mar", "Astana", "150500"]
]

filename = 'befor3.csv'
with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    for row in data:
        writer.writerow(row)

with open('befor3.csv', 'r') as file:
    print(file.read())

print("-----------------------")

month_mapping = {
    'Jan': '01-01', 'Feb': '02-01', 'Mar': '03-01',
    'Apr': '04-01', 'May': '05-01', 'Jun': '06-01',
    'Jul': '07-01', 'Aug': '08-01', 'Sep': '09-01',
    'Oct': '10-01', 'Nov': '11-01', 'Dec': '12-01'
}

input_filename = 'befor3.csv'
output_filename = 'after3.csv'

with open(input_filename, 'r') as infile, open(output_filename, 'w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    
    header = next(reader)
    writer.writerow(["year", "region", "value"])

    for row in reader:
        year = row[0]
        month_abbrev = row[1]
        day = month_mapping.get(month_abbrev, '01-01')
        updated_date = f'{year}-{day}'
        writer.writerow([updated_date, row[2], row[3]])

with open('after3.csv', 'r') as file:
    print(file.read())