from selenium import webdriver
from bs4 import BeautifulSoup
import csv

options = webdriver.ChromeOptions()
options.binary_location = "/path/to/chromedriver"

driver = webdriver.Chrome(options=options)

driver.get('https://en.wikipedia.org/wiki/Demographics_of_Kazakhstan')

page_source = driver.page_source

driver.quit()


soup = BeautifulSoup(page_source, 'html.parser')

table = soup.find('table', {'class': 'wikitable'})

with open('wikitable.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)

    # Извлеките строки из таблицы и записывайте их в CSV файл
    for row in table.find_all('tr'):
        data = [cell.get_text(strip=True).replace(',', ' ').replace(' ', '') for cell in row.find_all(['th', 'td'])]
        csv_writer.writerow(data)

