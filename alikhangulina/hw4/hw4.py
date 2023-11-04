from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import csv

driver = webdriver.Chrome()
driver.get("https://en.wikipedia.org/wiki/Demographics_of_Kazakhstan")

html = driver.page_source

driver.close()

soup = BeautifulSoup(html, 'html.parser')

table = soup.find('table', {'class': 'wikitable'})
data = []
for row in table.find_all('tr'):
    row_data = []
    for cell in row.find_all(['th', 'td']):
        row_data.append(cell.get_text(strip=True))
    data.append(row_data)

with open('kazakhstan_demographics.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(data)

