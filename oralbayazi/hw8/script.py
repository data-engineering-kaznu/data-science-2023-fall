from bs4 import BeautifulSoup
import requests

# Загрузка веб-страницы
url = "https://en.wikipedia.org/wiki/Demographics_of_Kazakhstan"
response = requests.get(url)
data = response.text

# Создание объекта BeautifulSoup
soup = BeautifulSoup(data, 'html.parser')

# Поиск таблицы
table = soup.find('table', {'class': 'wikitable'})

# Извлечение данных из таблицы
data = []

for row in table.find_all('tr'):
    cols = row.find_all(['th', 'td'])
    cols = [col.get_text(strip=True) for col in cols]
    data.append(cols)

# Создание DataFrame из данных
import pandas as pd

df = pd.DataFrame(data[1:], columns=data[0])

# Сохранение в CSV
df.to_csv('population_of_kazakhstan.csv', index=False)