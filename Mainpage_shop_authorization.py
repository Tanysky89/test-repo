from selenium.webdriver.common.by import By
import allure
driver = None

@allure.epic("интернет - магазин") 
@allure.severity("blocker")

class shop_form_authorization:
    @allure.step("Открытие сайта")
    def __init__(self, driver):
        self._driver = driver
        self._driver.implicitly_wait(4)
        self._driver.get("https://www.saucedemo.com/")
    
    @allure.step("Ввод логина {username}")    
    def username_input(self, username):
        self._driver.find_element(By.ID, "user-name").send_keys(username)
       
    @allure.step("Ввод пароля {password}")       
    def password_input(self, password):
        self._driver.find_element(By.ID, "password").send_keys(password)
    
    @allure.step("Нажатие кнопки входа")   
    def check_input(self):
        self._driver.find_element(By.ID, "login-button").click()

