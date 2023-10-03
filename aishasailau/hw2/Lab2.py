import csv

data = [
    ["year", "region", "value"],
    ["2022-Feb", "Almaty", "130500"],
    ["2022-Feb", "Astana", "150500"],
    ["2022-Mar", "Almaty", "150500"],
    ["2022-Mar", "Astana", "150500"]
]

filename = 'before2.csv'
with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    for row in data:
        writer.writerow(row)

with open('before2.csv', 'r') as file:
    print(file.read())

print("-----------------------")

input_filename = 'before2.csv'
output_filename = 'after2.csv'
d = {
    'Jan': '01-01', 'Feb': '02-01', 'Mar': '03-01',
    'Apr': '04-01', 'May': '05-01', 'Jun': '06-01',
    'Jul': '07-01', 'Aug': '08-01', 'Sep': '09-01',
    'Oct': '10-01', 'Nov': '11-01', 'Dec': '12-01'
}

with open(input_filename, 'r') as infile, open(output_filename, 'w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    header = next(reader)
    header[0] = 'year'
    writer.writerow(header)
    for row in reader:
        year = row[0][:4]  
        month_abbrev = row[0][5:8]
        day = d.get(month_abbrev, '01-01')
        row[0] = f'{year}-{day}'
        
        writer.writerow(row)
with open('after2.csv', 'r') as file:
    print(file.read())