import csv


data = [
    ['2022', 'Feb', 'Almaty', '130500'],
    ['2022', 'Feb', 'Astana', '150500'],
    ['2022', 'Mar', 'Almaty', '150500'],
    ['2022', 'Mar', 'Astana', '150500'],
]
file_name = 'output.csv'
with open(file_name, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(data[0])
    csvwriter.writerows(data[1:])
column_to_delete = 1
for row in data:
    del row[column_to_delete]
for row in data:
    print(row)
new_data_1 = ['2022-02-01',  'Almaty', '130500']
new_data_2 = ['2022-02-01',  'Astana', '150500']
new_data_3 = ['2022-03-01', 'Almaty', '150500']
new_data_4 = ['2022-03-01',  'Astana', '150500']
new_data = [new_data_1, new_data_2, new_data_3, new_data_4]
file_name='result.csv'
with open(file_name, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(new_data[0])
    csvwriter.writerows(new_data[1:])


