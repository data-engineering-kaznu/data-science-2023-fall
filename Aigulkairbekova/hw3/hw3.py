import csv
data=[['year','month','region','value'],
      ['2022','Feb','Almaty','130500'],
      ['2022','Feb','Astana','150500'],
      ['2022','Mar','Almaty','150500'],
      ['2022','Mar','Astana','150500']]

with open('hw3.csv', 'w') as f:
    writer = csv.writer(f)
    for row in data:
        writer.writerow(row)

with open('hw3.csv') as f:
    print(f.read())