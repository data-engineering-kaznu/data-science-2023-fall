import csv

d = {
    'Jan': '-01-01', 'Feb': '-02-01', 'Mar': '-03-01', 'Apr': '-04-01',
    'May': '-05-01', 'Jun': '-06-01', 'Jul': '-07-01', 'Aug': '-08-01',
    'Sep': '-09-01', 'Oct': '-10-01', 'Nov': '-11-01', 'Dec': '-12-01'
}

with open('source_data.csv', 'r', newline='') as f_source:
    reader = csv.reader(f_source, delimiter=',')
    next(reader, None)
    data = []

    for row in reader:
        month = row[1].strip()
        year = row[0] + d.get(month, '')
        row = [year, row[2], row[3]]
        data.append(row)

with open('result.csv', 'w', newline='') as f_result:
    writer = csv.writer(f_result)
    writer.writerow(['data', 'region', 'value'])
    writer.writerows(data)