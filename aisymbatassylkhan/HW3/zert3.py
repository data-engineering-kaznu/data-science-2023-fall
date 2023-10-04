import csv

# Specify the path to your CSV file
csv_file_path = 'original.csv'
csv_file_write = 'result.csv'

# Open the CSV file and create a CSV reader and writer objects
with open(csv_file_path, 'r', newline='') as csv_file, open(csv_file_write, 'w', newline='') as csv_file1:
    csv_reader = csv.reader(csv_file)
    csv_write = csv.writer(csv_file1)

    data = []
    # Read data from file and append it to the 'data' list
    for row in csv_reader:
        data.append(row)

    # Modify the header row to replace "year" with "date"
    header = data[0]
    header[0] = "date"

    # Change data in the list
    for row in data[1:]:
        if row[0][:4].isalnum():
            if row[0][5:] == 'Feb':
                row[0] = row[0][:4] + '-02-01'
            else:
                row[0] = row[0][:4] + '-03-01'

    # Write modified data, including the updated header, to the CSV file
    csv_write.writerows(data)




