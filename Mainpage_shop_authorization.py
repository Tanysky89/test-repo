from selenium.webdriver.common.by import By

driver = None


class shop_form_authorization:
    def __init__(self, driver):
        self._driver = driver
        self._driver.implicitly_wait(4)
        self._driver.get("https://www.saucedemo.com/")

    def username_input(self, username):
        self._driver.find_element(By.ID, "user-name").send_keys(username)
       
    def password_input(self, password):
        self._driver.find_element(By.ID, "password").send_keys(password)
    
    def check_input(self):
        self._driver.find_element(By.ID, "login-button").click()

