import csv
with open('source_data.csv', 'r', newline='') as f_source:
    reader = csv.reader(f_source)
    next(reader, None)
    data = []
    month = ['-Jan', '-Feb', '-Mar', '-Apr', '-May', '-Jun', '-Jul', '-Aug', '-Sep', '-Oct', '-Nov', '-Dec']

    for row in reader:
        if row[0][4:] in month:
            year = row[0][:4] + '-' + str(month.index(row[0][4:]) + 1).zfill(2) + '-01'
        row = [year, row[1], row[2]]
        data.append(row)

with open('result.csv', 'w', newline='') as f_result:
    writer = csv.writer(f_result)
    writer.writerow(['year', 'region', 'value'])
    writer.writerows(data)



