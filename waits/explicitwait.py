import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

obj1=Service()
driver=webdriver.Chrome(service=obj1)

wait=WebDriverWait(driver,10)

driver.get("https://demo.nopcommerce.com/register")

male_checkbox=driver.find_element(By.ID,"gender-male")

#Explicit wait commmand :

wait.until(expected_conditions.element_to_be_clickable(male_checkbox))

male_checkbox.click()


firstname=driver.find_element(By.ID,"FirstName")

wait.until(expected_conditions.visibility_of(firstname))

firstname.send_keys("prakash")

driver.find_element(By.ID,"LastName").send_keys("kulkarni")

#driver.find_element(By.ID,"FirstName").send_keys("prakash")

print(male_checkbox.is_selected())

time.sleep(5)

