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

#Creating object of webdriver wait to use later in code
wait=WebDriverWait(driver,10)

driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://testautomationpractice.blogspot.com/")

#Click on the button which opens a new window

switch_click=driver.find_element(By.XPATH,"//button[@onclick='myFunction()']")

#Store the window handle of current/origonal window before opening a new window
original_window=driver.current_window_handle

switch_click.click()

#waits till new window is opened

wait.until(expected_conditions.number_of_windows_to_be(2))

#This methods gets all the window handles of all the open windows
all_windows=driver.window_handles

#loop to iterate over each window and switches if not the original winodw
for single_window_id in all_windows:
    if(single_window_id!=original_window):
        driver.switch_to.window(single_window_id)
        break

#click on eles in new window

driver.find_element(By.LINK_TEXT,"Desktops").click()
time.sleep(1)

driver.find_element(By.LINK_TEXT,"Laptops & Notebooks").click()
time.sleep(1)

driver.find_element(By.LINK_TEXT,"Tablets").click()
time.sleep(1)

driver.find_element(By.LINK_TEXT,"Software").click()
time.sleep(1)

driver.find_element(By.LINK_TEXT,"MP3 Players").click()
time.sleep(1)


#closes the switched window
driver.close()

#switches back to original window
driver.switch_to.window(original_window)


driver.quit()