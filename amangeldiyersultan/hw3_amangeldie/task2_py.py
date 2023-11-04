import csv
from datetime import datetime

with open('task3_1.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    field = ["year", "region", "value"]

    writer.writerow(field)
    writer.writerow(["2022", "Feb", "Almaty", "130050"])
    writer.writerow(["2022", "Feb", "Astana", "130050"])
    writer.writerow(["2022", "Mar", "Almaty", "130050"])
    writer.writerow(["2022", "Mar", "Astana", "130050"])

input_file_path = 'task3_1.csv'
output_file_path = 'task3_2.csv'

date_column_index = 0

current_date_format = '%Y%b'

new_date_format = '%Y-%m-%d'

with open(input_file_path, 'r', newline='') as input_file, \
        open(output_file_path, 'w', newline='') as output_file:
    csvreader = csv.reader(input_file)
    csvwriter = csv.writer(output_file)

    for row in csvreader:
        try:
            old_date_str = row[0] + row[1]
            new_date_str = datetime.strptime(old_date_str, current_date_format).strftime(new_date_format)
            row[0] = new_date_str
            row.pop(1)
            csvwriter.writerow(row)
        except ValueError:
            csvwriter.writerow(row)

with open('task3_2.csv', 'r', newline='') as csvfile:
    csvreader = csv.reader(csvfile)

    for row in csvreader:
        print(row)
