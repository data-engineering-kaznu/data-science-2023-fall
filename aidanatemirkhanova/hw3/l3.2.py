import csv
input_filename = 'lab3.csv'
output_filename = 'mlab3.csv'
dictionary = {'Feb':'02-01','Mar':'03-01','Apr':'04-01',
              'May':'05-01','Jun':'06-01','Jul':'07-01',
              'Aug':'08-01','Sep':'09-01','Oct':'10-01',
              'Nov':'11-01','Dec':'12-01','Jan':'01-01'}
with open(input_filename, 'r') as infile, open(output_filename, 'w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    
    header = next(reader)
    writer.writerow(["year", "region", "value"])

    for row in reader:
        year = row[0]
        y_m_join = row[1]
        day = dictionary.get(y_m_join, '01-01')
        updated_date = f'{year}-{day}'
        writer.writerow([updated_date, row[2], row[3]])
        
with open('mlab3.csv', 'r') as file:
    print(file.read())
