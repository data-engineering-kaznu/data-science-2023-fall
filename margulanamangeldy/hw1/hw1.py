import csv

st = [['year','region','value'],
      ['2020','Almaty','130500'],
      ['2020','Almaty','130500']]
print(st)
for i in range(len(st)):
    st[i][0] = st[i][0] + '-01-01'

with open('file1.csv','w') as output:
    writer = csv.writer(output)
    writer.writerow(st)
