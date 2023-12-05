import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

obj1=Service()
driver=webdriver.Chrome(service=obj1)

driver.maximize_window()

driver.get("https://demo.nopcommerce.com/login")

links=driver.find_elements(By.XPATH,"//div[@class='footer-upper']/div/ul/li")

print(len(links))

for i in links:
    print(i.text)

time.sleep(4)

driver.close()




#


