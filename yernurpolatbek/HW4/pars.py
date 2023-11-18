from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions as Options
import csv

driver = webdriver.Chrome(options=Options())

driver.get("https://en.wikipedia.org/wiki/Demographics_of_Kazakhstan")

tbody = driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[6]')

data =  []

header_row = tbody.find_element(By.TAG_NAME, "thead").find_element(By.TAG_NAME, "tr")
header_data = [header.text for header in header_row.find_elements(By.TAG_NAME, "th")]
data.append(header_data)

for tr in tbody.find_elements(By.XPATH, ".//tr"):
    row = [item.text for item in tr.find_elements(By.TAG_NAME, "td")]
    data.append(row)

data.pop(1)
data[0][0] = 'Year'

with open('demography.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data[][])

driver.quit()