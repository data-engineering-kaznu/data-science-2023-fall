from bs4 import BeautifulSoup
import requests

url = "https://en.wikipedia.org/wiki/Demographics_of_Kazakhstan"
response = requests.get(url)
data = response.text

soup = BeautifulSoup(data, 'html.parser')

table = soup.find('table', {'class': 'wikitable'})

data = []

for row in table.find_all('tr'):
    cols = row.find_all(['th', 'td'])
    cols = [col.get_text(strip=True) for col in cols]
    data.append(cols)

import pandas as pd

df = pd.DataFrame(data[1:], columns=data[0])

df.to_csv('population_kazakhstan.csv', index=False)
