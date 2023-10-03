import csv


# Откройте CSV-файл для чтения и создайте CSV-писатель для записи
with open('TAsk2.csv', 'r') as i, open('task2-result.csv', 'w', newline='') as o:
    csv_reader = csv.reader(i)
    csv_write = csv.writer(o)
    date = []
    for row in csv_reader:
        date.append(row)

    for row in date:
        if row[0][:4].isalnum():
            match row[0][5:]:
                case 'Jan':
                    row[0] = row[0][:4] + '-01-01'
                case 'Feb':
                    row[0] = row[0][:4] + '-02-01'
                case 'Mar':
                    row[0] = row[0][:4] + '-03-01'
                case 'Apr':
                    row[0] = row[0][:4] + '-04-01'
                case 'May':
                    row[0] = row[0][:4] + '-05-01'
                case 'Jun':
                    row[0] = row[0][:4] + '-06-01'
                case 'Jul':
                    row[0] = row[0][:4] + '-07-01'
                case 'Aug':
                    row[0] = row[0][:4] + '-08-01'
                case 'Sep':
                    row[0] = row[0][:4] + '-09-01'
                case 'Oct':
                    row[0] = row[0][:4] + '-10-01'
                case 'Nov':
                    row[0] = row[0][:4] + '-11-01'
                case 'Dec':
                    row[0] = row[0][:4] + '-12-01'


    # write data to csv file
    for row in date:
        csv_write.writerow(row)
