from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


driver.get("http://uitestingplayground.com/textinput")
text_input = driver.find_element(By.ID, "newButtonName")
text = 'SkyPro'
text_input.send_keys(text)

driver.find_element(By.ID, "updatingButton").click()
txt = driver.find_element(By.ID, "updatingButton").text


print(txt)

driver.quit()
