import csv

# Specify the path to your CSV file
csv_file_path = 'hw2.csv'
csv_file_write = 'hw22.csv'

# Open the CSV file and create a CSV reader object
with open(csv_file_path, 'r') as csv_file, open(csv_file_write, 'w', newline='') as csv_file1:
    csv_reader = csv.reader(csv_file)
    csv_write = csv.writer(csv_file1)

    date = []
    # Read data from file and appent it to list date
    for row in csv_reader:
        date.append(row)

    # Change data in our list
    for row in date:
        if row[0][:4].isalnum():
            if row[0][5:] == 'Feb':
                row[0] = row[0][:4] + '-02-01'
            elif row[0][5:] == 'Mar':
                row[0] = row[0][:4] + '-03-01'
            elif row[0][5:] == 'May':
                row[0] = row[0][:4] + '-05-01'
            elif row[0][5:] == 'June':
                row[0] = row[0][:4] + '-06-01'
            elif row[0][5:] == 'Jule':
                row[0] = row[0][:4] + '-07-01'
            elif row[0][5:] == 'Aug':
                row[0] = row[0][:4] + '-08-01'
            elif row[0][5:] == 'Sep':
                row[0] = row[0][:4] + '-09-01'
            elif row[0][5:] == 'Oct':
                row[0] = row[0][:4] + '-10-01'
            elif row[0][5:] == 'Nov':
                row[0] = row[0][:4] + '-11-01'
            elif row[0][5:] == 'Dec':
                row[0] = row[0][:4] + '-12-01'
            elif row[0][5:] == 'Jan':
                row[0] = row[0][:4] + '-01-01'
            else: row[0] = row[0][:4] + '-04-01'


                

    # write data to csv file
    for row in date:
        csv_write.writerow(row)
    
