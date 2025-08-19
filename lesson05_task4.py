from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.common.by import By
from time import sleep

options = Options()
firefox_profile = FirefoxProfile()
firefox_profile.set_preference("javascript.enabled", False)
options.profile = firefox_profile

driver = webdriver.Firefox(options=options)
driver.get("http://the-internet.herokuapp.com/login")

username_input = driver.find_element(By.CSS_SELECTOR, "input[type='text']")
username = 'tomsmith'
username_input.send_keys(username)


password_input = driver.find_element(By.ID, "password")
password = 'SuperSecretPassword!'
password_input.send_keys(password)
sleep(5)

check_input = driver.find_element(By.CLASS_NAME, "radius")
check_input.click()

print(driver.find_element(By.ID, "flash").text)

driver.quit()
