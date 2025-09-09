from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from Mainpage_calc import calculator_form


def test_calc():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    MyCalc = calculator_form(driver)
    MyCalc.input_delay("45")
    MyCalc.find_element_n_click("btn btn-outline-primary","7")
    MyCalc.find_element_n_click("operator btn btn-outline-success","+")
    MyCalc.find_element_n_click("btn btn-outline-primary","8")
    MyCalc.find_element_n_click("btn btn-outline-warning","=")
    MyCalc.get_result_n_compare("15")
    MyCalc.quit_driver()
