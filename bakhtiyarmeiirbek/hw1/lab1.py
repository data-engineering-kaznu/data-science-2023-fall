import csv

lab1= [['year', 'region', 'value'],
       ['2020', 'Almaty', '130500'],
       ['2021', 'Almaty', '150500']]

with open('lab1.csv', "w") as csvfile:
       writer = csv.writer(csvfile, delimiter= ',')
       for row in lab1:
              writer.writerow(row)


with open('lab1.csv', "w") as csvfile:
       writer = csv.reader(csvfile, delimiter= ',')
       for row in lab1:
              row[0]= row[0]+ '01-01'
              .readerr(r



# csv.reader
# row[0] = row[0]+'01-01'
# csv writer