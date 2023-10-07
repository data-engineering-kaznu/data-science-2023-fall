import csv
slovar = {"Jan": "-01-01", "Feb": "-02-01",
           "Mar": "-03-01", "Apr": "-04-01",
           "May": "-05-01", "Jun": "-06-01",
           "Jul": "-07-01", "Aug": "-08-01",
           "Sep": "-09-01", "Oct": "-10-01",
           "Nov": "-11-01", "Dec": "-12-01",}
with open('table.csv', 'r',  newline='') as b:
    reader = csv.reader(b, delimiter=',')
    next(reader, None)
    data = []
     
    for row in reader:
       month = row[1].strip()
       year = row[0] + slovar.get(month)
       row = [year, row[2], row[3]]
       data.append(row)

with open('result.csv', 'w', newline='') as a:
  writer = csv.writer(a)
  writer.writerow(['data', 'region', 'value'])
  writer.writerows(data)

