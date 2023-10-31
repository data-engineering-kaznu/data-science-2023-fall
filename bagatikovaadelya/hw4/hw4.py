import requests
from bs4 import BeautifulSoup
import pandas as pd
url = "https://en.wikipedia.org/wiki/Demographics_of_Kazakhstan"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
table = soup.find("table", {"class": "wikitable"})
rows = table.find_all("tr")
data = []
for row in rows:
    cols = row.find_all(["th", "td"])
    cols = [col.get_text(strip=True) for col in cols]
    data.append(cols)
df = pd.DataFrame(data[1:], columns=data[0])
df.to_csv("population_kazakhstan.csv", index=False)
