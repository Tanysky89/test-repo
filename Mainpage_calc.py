from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class calculator_form:
    def __init__(self, driver):
        self._driver = driver
        self._driver.implicitly_wait(45)
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def input_delay(self, delay_txt):
        delay_input = self._driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys(delay_txt)

    def find_element_n_click(self, search_str, button_str):
        find_string = "//span[@class='" + search_str + "' and text()='" + button_str + "']"
        self._driver.find_element(By.XPATH, find_string).click()

    def get_result_n_compare(self, num_str):
        find_string = "//div[@class='screen' and text()='" + num_str + "']"
        res = self._driver.find_element(By.XPATH, find_string)
        assert res.text == num_str, "Результаты не совпадают!"
        print(res.text)

    def quit_driver(self):
        self._driver.quit()
