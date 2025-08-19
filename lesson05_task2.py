from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/dynamicid")
check_input = driver.find_element(By.CLASS_NAME, "btn-primary")
check_input.click()

sleep(5)
driver.quit()
