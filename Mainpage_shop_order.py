from selenium.webdriver.common.by import By
import allure

driver = None

@allure.epic("интернет - магазин") 
@allure.severity("blocker")

class shop_form_order:
    @allure.step("Страница оформления заказа")
    def __init__(self, driver):
        self._driver = driver
        self._driver.implicitly_wait(4)
        self._driver.get("https://www.saucedemo.com/checkout-step-one.html")

    @allure.step("Ввод имени покупателя")
    def firstname(self, firstname):
        self._driver.find_element(By.ID, "first-name").send_keys(firstname)

    @allure.step("Ввод фамилии покупателя")
    def lastname(self, lastname):
        self._driver.find_element(By.ID, "last-name").send_keys(lastname)
        
    @allure.step("Ввод почтового индекса покупателя")    
    def zip(self, zip):
        self._driver.find_element(By.ID, "postal-code").send_keys(zip)

    @allure.step("Вывод итоговой стоимости товаров")   
    def prz(self):
        self._driver.find_element(By.ID, "continue").click()
        priceTotal = self._driver.find_element(By.CLASS_NAME, 'summary_total_label').text
        return priceTotal
      
    @allure.step("Закрытие сессии")  
    def quit_driver(self):
        self._driver.quit()
