import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


obj1=Service()
driver=webdriver.Chrome(service=obj1)
driver.get("https://demo.nopcommerce.com/register")

male_checkbox=driver.find_element(By.ID,"gender-male")

male_checkbox.click()

driver.find_element(By.ID,"FirstName").send_keys("prakash")

driver.find_element(By.ID,"LastName").send_keys("kulkarni")

#driver.find_element(By.ID,"FirstName").send_keys("prakash")

print(male_checkbox.is_selected())

time.sleep(5)


#https://demo.nopcommerce.com/register


