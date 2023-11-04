from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import csv
driver = webdriver.Chrome()

def main():
    driver.get('https://en.wikipedia.org/wiki/Demographics_of_Kazakhstan#Population_of_Kazakhstan_1897–2018')  
    table=driver.find_element(By.XPATH,'//*[@id="mw-content-text"]/div[1]/table[5]')
    data=[]
    header_row = table.find_element(By.TAG_NAME, 'tr')
    headers = [header.text for header in header_row.find_elements(By.TAG_NAME, 'th')]
    data.append(headers)
    
    for row in table.find_elements(By.TAG_NAME, 'tr')[1:]: 
        row_data = [item.text for item in row.find_elements(By.TAG_NAME, 'td')]
        data.append(row_data)
    print(data)
    with open('out.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile,delimiter=',')
        csvwriter.writerows(data)
if __name__=='__main__':
    main()