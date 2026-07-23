from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

driver.get("https://www.saucedemo.com/")

wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

print(driver.current_url)

driver.quit()

# Returns the inventory website after correct login. Test for other types of users.

driver2 = webdriver.Chrome()
driver2.get("https://www.saucedemo.com/")

wait2 = WebDriverWait(driver2, 10)

wait2.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("locked_out_user")
driver2.find_element(By.ID, "password").send_keys("secret_sauce")
driver2.find_element(By.ID, "login-button").click()
