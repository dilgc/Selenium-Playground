from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com/")

print(driver.title)

username_field = driver.find_element(By.ID, "user-name")
login_button = driver.find_element(By.ID, "login-button")


driver.quit()