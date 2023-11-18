from bs4 import BeautifulSoup
import requests
import pandas as pd

data = requests.get("https://en.wikipedia.org/wiki/Demographics_of_Kazakhstan").text

table = BeautifulSoup(data, 'html.parser').find('table', {'class': 'wikitable'})

data1 = []

for row in table.find_all('tr'):
    cols = row.find_all(['th', 'td'])
    cols = [col.get_text(strip=True) for col in cols]
    data1.append(cols)

df = pd.DataFrame(data1[1:], columns=data1[0])

# Сохранение в CSV
df.to_csv('population_kazakhstan.csv', index=False)