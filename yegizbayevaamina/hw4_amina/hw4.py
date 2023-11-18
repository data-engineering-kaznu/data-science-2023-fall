from bs4 import BeautifulSoup
import requests
import pandas as pd
url = "https://en.wikipedia.org/wiki/Demographics_of_Kazakhstan"
response = requests.get(url)
data = response.text

# BeautifulSoup объектін құру
soup = BeautifulSoup(data, 'html.parser')

# Кестені іздеу
table = soup.find('table', {'class': 'wikitable'})

# Кестеден деректерді алу
data = []

for row in table.find_all('tr'):
    cols = row.find_all(['th', 'td'])
    cols = [col.get_text(strip=True) for col in cols]
    data.append(cols)

df = pd.DataFrame(data[1:], columns=data[0])

df.to_csv('population_of_kazakhstan.csv', index=False)
