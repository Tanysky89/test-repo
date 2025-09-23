from selenium.webdriver.common.by import By
driver = None
import allure

@allure.epic("интернет - магазин") 
@allure.severity("blocker")


class shop_form_basket:
    @allure.step("Главная страница магазина")
    def __init__(self, driver):
        self._driver = driver
        self._driver.implicitly_wait(4)
        self._driver.get("https://www.saucedemo.com/cart.html")
        
    @allure.step("Вывод данных о содержимом корзины")
    def comparison(self):
        txt = self._driver.find_element(By.CLASS_NAME, 'cart_list').text
        return txt
    
    @allure.step("Нажатие кнопки Checkout") 
    def find_element_n_click(self, str):
        self._driver.find_element(By.ID, str).click()
