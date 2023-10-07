import csv
input_filename = 'lab2.csv'
output_filename = 'mlab2.csv'

dictionary = {'Feb':'02-01','Mar':'03-01','Apr':'04-01',
              'May':'05-01','Jun':'06-01','Jul':'07-01',
              'Aug':'08-01','Sep':'09-01','Oct':'10-01',
              'Nov':'11-01','Dec':'12-01','Jan':'01-01'}
with open(input_filename, 'r') as file, open(output_filename, 'w', newline='') as file1:
    reader = csv.reader(file)
    writer = csv.writer(file1)
    
    header = next(reader)
    writer.writerow(header)
    
    for row in reader:
        row[0]=row[0][:-3]+dictionary[row[0][-3:]]
        writer.writerow(row)

