# Home work 3 
Талғатұлы Әділ  
Наука о данных  
3 курс  


    import csv
* Подключаем пакет csv
     

    with open('source_data.csv', 'r', newline='') as f_source:
        reader = csv.reader(f_source, delimiter=',')
        next(reader, None)
* Открываем файл 'source_data.csv' для чтения и создаем объект f_source для работы с ним.
* И создаем объект reader для чтения CSV файла.
* пропускаем первую строку где у нас написаны названия столбцов
 

    data = []
    month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
* Создаем пустой список data, в который будем добавлять измененные данные.
* И создаем список month, который содержит названия месяцев.


    for row in reader:
        year = row[0] + '-' + str(month.index(row[1]) + 1).zfill(2) + '-01'
        row = [year, row[2], row[3]]
        data.append(row)
* Проходимся по каждой строке в CSV файле
* Создаем переменную year, в которой хранятся данные про дату 
* Заменяем в текущей строке row данные на новые
* Добавляем новую строку в список data, который заранее мы уже открыли


    with open('result.csv', 'w', newline='') as f_result:
        writer = csv.writer(f_result)
        writer.writerow(['year', 'region', 'value'])
        writer.writerows(data)
* Открываем файл 'source_data.csv' для записи изменненных данных и создаем объект f_result для работы с ним
* И создаем объект writer для записи данных в CSV файл
* Записываем заголовок который мы ранее убрали 
* Записываем все измененные данные в csv файл