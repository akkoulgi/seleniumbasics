#

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


obj1=Service()
driver=webdriver.Chrome(service=obj1)

driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://testautomationpractice.blogspot.com/")

prompt=driver.find_element(By.XPATH,"//button[@onclick='myFunctionPrompt()']")

prompt.click()

time.sleep(3)

alert=Alert(driver)

alert.send_keys("The alert is working fine")

alert_text=alert.text

print(alert_text)

time.sleep(2)
alert.accept()
#alert.dismiss()


time.sleep(1)


