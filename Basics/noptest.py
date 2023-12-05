from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

obj1=Service()
driver=webdriver.Chrome(service=obj1)

driver.implicitly_wait(5)

driver.get("https://demo.nopcommerce.com/login")

driver.find_element(By.ID,"Email").send_keys("akshay.koulgi@gmail.com")

driver.find_element(By.ID,"Password").send_keys("admin123")

driver.find_element(By.XPATH,"//button[text()='Log in']").click()

