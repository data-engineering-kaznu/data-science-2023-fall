import csv

months = {" Jan":"-01-01", " Feb":"-02-01", " Mar":"-03-01", # dictionary for month conversion
          " Apr":"-04-01", " May":"-05-01", " Jun":"-06-01",
          " Jul":"-07-01", " Aug":"-08-01", " Sep":"-09-01",
          " Oct":"-10-01", " Nov":"-11-01", " Dec":"-12-01"}

with open('source.csv', 'r') as input_file, open("result.csv", 'w', newline="") as output_file:
    reader = csv.reader(input_file) 
    writer = csv.writer(output_file)

    header = next(reader) # operations on column names
    del header[1]
    writer.writerow(header)

    for row in reader: 
        row[0] = row[0] + months[row[1]] # concatenate year and modified month
        del row[1] # delete month column
        writer.writerow(row) # write row to output file