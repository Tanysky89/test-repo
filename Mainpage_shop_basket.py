from selenium.webdriver.common.by import By
driver = None


class shop_form_basket:
    def __init__(self, driver):
        self._driver = driver
        self._driver.implicitly_wait(4)
        self._driver.get("https://www.saucedemo.com/cart.html")
  
    def comparison(self):
        txt = self._driver.find_element(By.CLASS_NAME, 'cart_list').text
        return txt
     
    def find_element_n_click(self, str):
        self._driver.find_element(By.ID, str).click()
