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
driver.get("http://the-internet.herokuapp.com/inputs")


number_input = driver.find_element(By.CSS_SELECTOR, "input[type='number']")

number = 'Sky'
number_input.send_keys(number)
sleep(5)
number_input.clear()

number = 'Pro'
number_input.send_keys(number)
sleep(5)

driver.quit()
