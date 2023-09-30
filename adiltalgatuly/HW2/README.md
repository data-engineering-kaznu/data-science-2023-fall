# HOME WORK 1

    with open('source_data.csv', 'r', newline='') as f_source:
    reader = csv.reader(f_source)
* В этих строках я открываю файл source_data.csv для чтения данных в ней


    data = []
* Здесь я открыл новый список для измененных данных

 
            for row in reader:
        if row[0][4:] in month:
            year = row[0][:4] + '-' + str(month.index(row[0][4:]) + 1).zfill(2) + '-01'
        row = [year, row[1], row[2]]
        data.append(row)
* В этом цикле я прохожу по каждой строке в файле source_data.csv и изменяю формат даты, а также удаляю ненужные не нужные элементы с строк


    with open('result.csv', 'w', newline='') as f_result:
    writer = csv.writer(f_result)
    writer.writerow(['year', 'region', 'value'])
    writer.writerows(data)
* В этих строках я открываю файл result.csv для записи измененных данных в него