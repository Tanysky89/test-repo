from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
edge_driver_path = r'C:\Program Files\Edge\msedgedriver.exe'
driver = webdriver.Edge(service=EdgeService(edge_driver_path)) 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color

driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

Firstname_input = driver.find_element(By.NAME, 'first-name')
Firstname = 'Иван'
Firstname_input.send_keys(Firstname)

Lastname_input = driver.find_element(By.NAME, 'last-name')
Lastname = 'Петров'
Lastname_input.send_keys(Lastname)

address_input = driver.find_element(By.NAME, 'address')
address = 'Ленина, 55-3'
address_input.send_keys(address)

Email_input = driver.find_element(By.NAME, 'e-mail')
Email = 'test@skypro.com'
Email_input.send_keys(Email)

Phone_input = driver.find_element(By.NAME, 'phone')
Phone = '+7985899998787'
Phone_input.send_keys(Phone)

Zip_input = driver.find_element(By.NAME, 'zip-code')
Zip = ''
Zip_input.send_keys(Zip)

City_input = driver.find_element(By.NAME, 'city')
City = 'Москва'
City_input.send_keys(City)

Country_input = driver.find_element(By.NAME, 'country')
Country = 'Россия'
Country_input.send_keys(Country)

Job_input = driver.find_element(By.NAME, 'job-position')
Job = 'QA'
Job_input.send_keys(Job)

Company_input = driver.find_element(By.NAME, 'company')
Company = 'SkyPro'
Company_input.send_keys(Company)

driver.find_element(By.CLASS_NAME, "btn.btn-outline-primary.mt-3").click()

login_button_colour = Color.from_string(driver.find_element(By.ID,'zip-code').value_of_css_property('background-color'))
login_button_background_colour = Color.from_string(driver.find_element(By.ID,'zip-code').value_of_css_property('background-color'))
assert login_button_background_colour.hex == '#f8d7da', 'Фон д.б. розовый'
print(login_button_background_colour.hex) 

login_button_colour = Color.from_string(driver.find_element(By.ID,'first-name').value_of_css_property('background-color'))
login_button_background_colour = Color.from_string(driver.find_element(By.ID,'first-name').value_of_css_property('background-color'))
assert login_button_background_colour.hex == '#d1e7dd', 'Фон д.б. зеленый'
print(login_button_background_colour.hex) 

login_button_colour = Color.from_string(driver.find_element(By.ID,'last-name').value_of_css_property('background-color'))
login_button_background_colour = Color.from_string(driver.find_element(By.ID,'last-name').value_of_css_property('background-color'))
assert login_button_background_colour.hex == '#d1e7dd', 'Фон д.б. зеленый'
print(login_button_background_colour.hex) 

login_button_colour = Color.from_string(driver.find_element(By.ID,'address').value_of_css_property('background-color'))
login_button_background_colour = Color.from_string(driver.find_element(By.ID,'address').value_of_css_property('background-color'))
assert login_button_background_colour.hex == '#d1e7dd', 'Фон д.б. зеленый'
print(login_button_background_colour.hex) 

login_button_colour = Color.from_string(driver.find_element(By.ID,'e-mail').value_of_css_property('background-color'))
login_button_background_colour = Color.from_string(driver.find_element(By.ID,'e-mail').value_of_css_property('background-color'))
assert login_button_background_colour.hex == '#d1e7dd', 'Фон д.б. зеленый'
print(login_button_background_colour.hex) 

login_button_colour = Color.from_string(driver.find_element(By.ID,'phone').value_of_css_property('background-color'))
login_button_background_colour = Color.from_string(driver.find_element(By.ID,'phone').value_of_css_property('background-color'))
assert login_button_background_colour.hex == '#d1e7dd', 'Фон д.б. зеленый'
print(login_button_background_colour.hex) 

login_button_colour = Color.from_string(driver.find_element(By.ID,'city').value_of_css_property('background-color'))
login_button_background_colour = Color.from_string(driver.find_element(By.ID,'city').value_of_css_property('background-color'))
assert login_button_background_colour.hex == '#d1e7dd', 'Фон д.б. зеленый'
print(login_button_background_colour.hex) 

login_button_colour = Color.from_string(driver.find_element(By.ID,'country').value_of_css_property('background-color'))
login_button_background_colour = Color.from_string(driver.find_element(By.ID,'country').value_of_css_property('background-color'))
assert login_button_background_colour.hex == '#d1e7dd', 'Фон д.б. зеленый'
print(login_button_background_colour.hex) 

login_button_colour = Color.from_string(driver.find_element(By.ID,'job-position').value_of_css_property('background-color'))
login_button_background_colour = Color.from_string(driver.find_element(By.ID,'job-position').value_of_css_property('background-color'))
assert login_button_background_colour.hex == '#d1e7dd', 'Фон д.б. зеленый'
print(login_button_background_colour.hex) 

login_button_colour = Color.from_string(driver.find_element(By.ID,'company').value_of_css_property('background-color'))
login_button_background_colour = Color.from_string(driver.find_element(By.ID,'company').value_of_css_property('background-color'))
assert login_button_background_colour.hex == '#d1e7dd', 'Фон д.б. зеленый'
print(login_button_background_colour.hex) 

driver.quit()