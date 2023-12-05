from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By



obj_service = Service()
driver= webdriver.Chrome(service=obj_service)
#driver=webdriver.Chrome("/Users/admin/Downloads/chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.find_element(By.NAME,"username").send_keys("Admin")
driver.find_element(By.NAME,"password").send_keys("admin123")
#driver.find_element(By.CLASS_NAME,"oxd-button").click()
# driver.find_element(By.ID)
# actual_title=driver.title
#
# expected="OrangeHrm"
#
# if actual_title==expected:
#     print("Title is verified")

print(driver.title)
print(driver.current_url)
#print(driver.page_source)


#driver.close()