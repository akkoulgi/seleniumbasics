import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

obj1=Service()
driver=webdriver.Chrome(service=obj1)

driver.maximize_window()

driver.get("https://demo.nopcommerce.com/login")

Email_textbox=driver.find_element(By.ID,"Email")

attribute1=Email_textbox.get_attribute("data-val-required")
name_attribute=Email_textbox.get_attribute("name")
id_attribute=Email_textbox.get_attribute("id")

time.sleep(4)

print(attribute1)
print(name_attribute)
print(id_attribute)

