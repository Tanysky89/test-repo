from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.common.by import By
options = Options()
firefox_profile = FirefoxProfile()
options.profile = firefox_profile

driver = webdriver.Firefox(options=options)


def test_shop():
    driver.get("https://www.saucedemo.com/")
    username_input = driver.find_element(By.ID, "user-name")
    username = 'standard_user'
    username_input.send_keys(username)

    password_input = driver.find_element(By.ID, "password")
    password = 'secret_sauce'
    password_input.send_keys(password)

    check_input = driver.find_element(By.ID, "login-button")
    check_input.click()

    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
    driver.find_element(By.ID, "shopping_cart_container").click()
    driver.find_element(By.ID, "checkout").click()

    firstname_input = driver.find_element(By.ID, "first-name")
    firstname = 'Tany'
    firstname_input.send_keys(username)

    lastname_input = driver.find_element(By.ID, "last-name")
    lastname = 'M'
    lastname_input.send_keys(username)

    zip_input = driver.find_element(By.ID, "postal-code")
    zip = '443101'
    zip_input.send_keys(password)
    driver.find_element(By.ID, "continue").click()

    PriceTotal = driver.find_element(By.CLASS_NAME, 'summary_total_label')

    assert PriceTotal.text == 'Total: $58.29', "Все не ок"
    print(PriceTotal.text)

    driver.quit()
