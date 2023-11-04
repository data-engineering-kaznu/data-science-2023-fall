import requests
from bs4 import BeautifulSoup
import csv

# Загрузка веб-страницы
url = "https://en.wikipedia.org/wiki/Demographics_of_Kazakhstan"
response = requests.get(url)
html = response.text

# Создание объекта BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Находим таблицу "Population of Kazakhstan 1897–2018" по заголовку
table = soup.find('span', {'id': 'Population_of_Kazakhstan_1897–2018'}).find_next('table')

# Открываем файл CSV для записи
with open('kazakhstan_population.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    # Извлекаем заголовки таблицы
    headers = [header.get_text(strip=True) for header in table.find_all('th')]
    writer.writerow(headers)

    # Извлекаем данные из таблицы и записываем их в CSV
    for row in table.find_all('tr')[1:]:
        columns = row.find_all(['th', 'td'])
        row_data = [column.get_text(strip=True) for column in columns]
        writer.writerow(row_data)

print("Успешно сохранены в kazakhstan_population.csv")
