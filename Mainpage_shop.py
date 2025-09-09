from selenium.webdriver.common.by import By
driver = None


class shop_form:
    def __init__(self, driver):
        self._driver = driver
        self._driver.implicitly_wait(4)
        self._driver.get("https://www.saucedemo.com/inventory.html")

    def find_element_n_click(self, str):
        self._driver.find_element(By.ID, str).click()
