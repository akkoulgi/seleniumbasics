import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


obj1=Service()
driver=webdriver.Chrome(service=obj1)

driver.implicitly_wait(5)

driver.get("https://testautomationpractice.blogspot.com/")

checkboxes=driver.find_elements(By.XPATH,"//div[@class='form-check form-check-inline']")

for i in range(len(checkboxes)):
        checkboxes[i].click()

time.sleep(5)