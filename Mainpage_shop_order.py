from selenium.webdriver.common.by import By

driver = None


class shop_form_order:
    def __init__(self, driver):
        self._driver = driver
        self._driver.implicitly_wait(4)
        self._driver.get("https://www.saucedemo.com/checkout-step-one.html")

    def firstname(self, firstname):
        self._driver.find_element(By.ID, "first-name").send_keys(firstname)

    def lastname(self, lastname):
        self._driver.find_element(By.ID, "last-name").send_keys(lastname)
        
    def zip(self, zip):
        self._driver.find_element(By.ID, "postal-code").send_keys(zip)

    def prz(self):
        self._driver.find_element(By.ID, "continue").click()
        priceTotal = self._driver.find_element(By.CLASS_NAME, 'summary_total_label').text
        return priceTotal
      
    def quit_driver(self):
        self._driver.quit()
