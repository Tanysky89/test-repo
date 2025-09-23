from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from Mainpage_calc import calculator_form
import allure

@allure.id("Lesson_10")
@allure.description("Проверка функциональности калькулятора")
@allure.feature("CREATE")
@allure.title("Выполнение сложения")

def test_calc():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    MyCalc = calculator_form(driver)
    
    with allure.step("Ввод данных в поле задержки"):
        MyCalc.input_delay("45")
    
    with allure.step("Ввод арифмитических данных"):
        MyCalc.find_element_n_click("btn btn-outline-primary","7")
        MyCalc.find_element_n_click("operator btn btn-outline-success","+")
        MyCalc.find_element_n_click("btn btn-outline-primary","8")
        MyCalc.find_element_n_click("btn btn-outline-warning","=")
    
    with allure.step("Вывод итогового результата"):
        MyCalc.get_result_n_compare("15")
    
    with allure.step("Закрытие сеанса"):
        MyCalc.quit_driver()
