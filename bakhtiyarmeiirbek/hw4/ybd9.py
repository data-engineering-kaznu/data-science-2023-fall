import requests
from bs4 import BeautifulSoup
import pandas as pd

# Загрузите веб-страницу с таблицей
url = "https://en.wikipedia.org/wiki/Demographics_of_Kazakhstan"
response = requests.get(url)

# Создайте объект BeautifulSoup для анализа HTML-кода
soup = BeautifulSoup(response.text, "html.parser")

# Найдите таблицу "Population of Kazakhstan 1897–2018"
table = soup.find("table", {"class": "wikitable"})
rows = table.find_all("tr")

data = []

for row in rows:
    cols = row.find_all(["th", "td"])
    cols = [col.get_text(strip=True) for col in cols]
    data.append(cols)

# Создайте DataFrame из данных
df = pd.DataFrame(data[1:], columns=data[0])  # Исключаем первую строку с заголовками

# Сохраните DataFrame в CSV файл
df.to_csv("population_kazakhstan.csv", index=False)

print("Таблица 'Population of Kazakhstan 1897–2018' сохранена в файл 'population_kazakhstan.csv'")