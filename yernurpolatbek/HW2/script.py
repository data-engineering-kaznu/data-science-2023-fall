import csv

months = {"Jan": "01-01", "Feb": "02-01", "Mar": "03-01",
          "Apr": "04-01", "May": "05-01", "Jun": "06-01",
          "Jul": "07-01", "Aug": "08-01", "Sep": "09-01",
          "Oct": "10-01", "Nov": "11-01", "Dec": "12-01"}

with open('HW2_prev.csv', 'r') as input, open('HW2.csv', 'w', newline='') as output:
    reader = csv.reader(input)
    writer = csv.writer(output)

    header = next(reader)
    writer.writerow(header)

    for row in reader:
        row[0] = row[0][0:-3] + months[row[0][-3:]]
        writer.writerow(row)

