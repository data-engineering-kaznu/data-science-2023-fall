import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from chromedriver_autoinstaller import install
install()

driver = webdriver.Chrome()

driver.get("https://en.wikipedia.org/wiki/Demographics_of_Kazakhstan")
table = driver.find_element("xpath", "/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/table[5]")
# Находим все строки в таблице
rows = table.find_elements(By.TAG_NAME,"tr")
with open("wikipedia_table_data.csv", mode="w", newline="") as file:
    writer = csv.writer(file)

    for row in rows:
        cells = row.find_elements(By.TAG_NAME,"td")
        row_data = [cell.text for cell in cells]
        writer.writerow(row_data)

driver.quit()
