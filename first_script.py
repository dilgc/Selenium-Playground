from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com/")

print(driver.title)

driver.get("https://www.youtube.com/")

print(driver.title)

driver.quit()