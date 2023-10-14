import csv

csv_file_path = 'hw3.csv'
csv_file_path_to_write = 'hw33.csv'
months = {
    'Jan': '01',
    'Feb': '02',
    'Mar': '03',
    'Apr': '04',
    'May': '05',
    'Jun': '06',
    'Jul': '07',
    'Aug': '08',
    'Sep': '09',
    'Oct': '10',
    'Nov': '11',
    'Dec': '12'
   
}

with open(csv_file_path, 'r') as csv_file, open(csv_file_path_to_write, 'w', newline='') as write_to:
    reader = csv.reader(csv_file)
    titles =next(reader)
    titles.remove("month")
    writer = csv.writer(write_to)

    print(f'Titles: {titles}')

    data = [titles]
    for i in reader:
        data1 = '-'.join([i[0],months[i[1]],'01'])
        data.append(
            [data1, i[2], i[3]]
        )
    writer.writerows(data)
