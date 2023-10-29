import requests
from bs4 import BeautifulSoup
import csv

url = 'https://en.wikipedia.org/wiki/Demographics_of_Kazakhstan'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    table = soup.find('table', {'class': 'wikitable'})
    
    if table:
        with open('kazakhstan_population.csv', 'w', newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)
            
            for row in table.find_all('tr'):
                columns = row.find_all(['th', 'td'])  
                if columns:
                    row_data = [column.get_text(strip=True) for column in columns]
                    writer.writerow(row_data)
                    print(', '.join(row_data))  

        print("Data has been written to 'kazakhstan_population.csv'")
    else:
        print("Table not found on the page.")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
