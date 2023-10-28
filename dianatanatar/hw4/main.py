import requests
from bs4 import BeautifulSoup
import csv

url = "https://en.wikipedia.org/wiki/Demographics_of_Kazakhstan"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find("table", {"class": "wikitable"})
with open("kazakhstan_population.csv", "w", newline='') as csv_file:
    writer = csv.writer(csv_file)
    headers = [header.text.strip() for header in table.findAll("th")]
    writer.writerow(headers)
    rows = table.findAll("tr")[1:]
    for row in rows:
        data = [cell.text.strip() for cell in row.findAll("td")]
        writer.writerow(data)
print()