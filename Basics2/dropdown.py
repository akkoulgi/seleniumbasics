import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


obj1=Service()
driver=webdriver.Chrome(service=obj1)

driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://testautomationpractice.blogspot.com/")

driver.execute_script("window.scrollTo(0,700)")

wait=WebDriverWait(driver,10)

country_dropdown=driver.find_element(By.XPATH,"//select[@class='form-control' and @id='country']")

wait.until(expected_conditions.visibility_of(country_dropdown))

select_obj =Select(country_dropdown)

select_obj.select_by_index(2)
time.sleep(1)
select_obj.select_by_value("usa")
time.sleep(1)
select_obj.select_by_visible_text("Germany")

time.sleep(4)

