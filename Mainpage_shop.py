from selenium.webdriver.common.by import By
driver = None
import allure

@allure.epic("интернет - магазин") 
@allure.severity("blocker")

class shop_form:
    @allure.step("Страница корзины")
    def __init__(self, driver):
        self._driver = driver
        self._driver.implicitly_wait(4)
        self._driver.get("https://www.saucedemo.com/inventory.html")

    @allure.step("Добавление товаров в корзину и переход в корзину")
    def find_element_n_click(self, str):
        self._driver.find_element(By.ID, str).click()
