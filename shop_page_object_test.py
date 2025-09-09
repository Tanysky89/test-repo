from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
options = Options()
firefox_profile = FirefoxProfile()
options.profile = firefox_profile
from Mainpage_shop_authorization import shop_form_authorization
from Mainpage_shop import shop_form
from Mainpage_shop_basket import shop_form_basket
from Mainpage_shop_order import shop_form_order


def test_shop():
    driver = webdriver.Firefox(options=options)
    
    Myauthorization = shop_form_authorization(driver)
    Myauthorization.username_input('standard_user')
    Myauthorization.password_input('secret_sauce')
    Myauthorization.check_input()
    
    MyShop = shop_form(driver)
    MyShop.find_element_n_click("add-to-cart-sauce-labs-backpack")
    MyShop.find_element_n_click("add-to-cart-sauce-labs-bolt-t-shirt")
    MyShop.find_element_n_click("add-to-cart-sauce-labs-onesie")
    MyShop.find_element_n_click("shopping_cart_container")
    
    Mybasket = shop_form_basket(driver)
    purchase = Mybasket.comparison()
    print(purchase)
    
    Mybasket.find_element_n_click("checkout")
    
    Myorder = shop_form_order(driver)
    Myorder.firstname('Tany')
    Myorder.lastname('M')
    Myorder.zip('443101')
    PriceTotal = Myorder.prz()
    assert PriceTotal == 'Total: $58.29', "Все не ок"
    print(PriceTotal)
    Myorder.quit_driver()
