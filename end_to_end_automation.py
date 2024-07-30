# automate a mobile website to check end to end automation
from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
print(driver.title)
driver.implicitly_wait(4)
driver.find_element(By.LINK_TEXT, "Shop").click()

mobiles = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

#print(mobiles)

for mob in mobiles:
    mobile_name = mob.find_element(By.XPATH, "div/h4/a").text
    if mobile_name == "Blackberry":
        mob.find_element(By.XPATH, "div/button").click()

driver.find_element(By.XPATH, "//li[@class='nav-item active']/a").click()
driver.find_element(By.XPATH, "//tbody/tr[3]/td[5]/button[@type='button']").click()
driver.find_element(By.ID, "country").send_keys("Ind")
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element(By.LINK_TEXT, "India").click()
driver.find_element(By.XPATH, "//label[@for='checkbox2']").click()
driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
Success_text = driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text

assert "Success! Thank you!" in Success_text
driver.close()


time.sleep(4)













#time.sleep(2)

