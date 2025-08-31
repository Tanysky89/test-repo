from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.implicitly_wait(45)
driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

number_input = driver.find_element(By.ID, "delay")
number_input.clear()
text = '45'
number_input.send_keys(text)

driver.find_element(By.XPATH, "//span[@class='btn btn-outline-primary' and text()='7']").click()
driver.find_element(By.XPATH, "//span[@class='operator btn btn-outline-success' and text()='+']").click()
driver.find_element(By.XPATH, "//span[@class='btn btn-outline-primary' and text()='8']").click()
driver.find_element(By.XPATH, "//span[@class='btn btn-outline-warning' and text()='=']").click()

res = driver.find_element(By.XPATH, "//div[@class='screen' and text()='15']")

assert res.text == '15', "Все не ок"
print(res.text)

driver.quit()
