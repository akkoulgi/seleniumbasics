from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

obj1=Service()
driver=webdriver.Chrome(service=obj1)

driver.maximize_window()

driver.get("https://www.myntra.com/")

driver.get("https://www.facebook.com/")


driver.back()
driver.forward()
driver.refresh()


