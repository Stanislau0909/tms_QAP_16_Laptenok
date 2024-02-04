import pytest
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def test_1(driver):
    driver.get("http://thedemosite.co.uk/login.php")
    element_input_login = "//input[@name='username']"
    input_login = driver.find_element(By.XPATH , element_input_login)
    input_login.send_keys("user1")

    element_input_password = "//input[@type='password']"
    input_login = driver.find_element(By.XPATH , element_input_password)
    input_login.send_keys("1234")

    element_button_submit = "//input[@type='button']"
    button_submit = driver.find_element(By.XPATH , element_button_submit)
    button_submit.click()

def test_2(driver):
    driver.get("https://demo.guru99.com/test/newtours/register.php")
    element_firstName = "//input[@name = 'firstName']"
    field_firstName = driver.find_element(By.XPATH , element_firstName)
    field_firstName.send_keys("Stanislau")
    element_lastName = "//input[@name = 'lastName']"
    field_lastName = driver.find_element(By.XPATH , element_lastName)
    field_lastName.send_keys("Laptsionak")
    element_phone = "//input[@name = 'phone']"
    field_phone = driver.find_element(By.XPATH , element_phone)
    field_phone.send_keys("7776556")
    element_email =  "//input[@id = 'userName']"
    field_email = driver.find_element(By.XPATH , element_email)
    field_email.send_keys("someemail@mail.ru")
    element_address = "//input[@name = 'address1']"
    field_address = driver.find_element(By.XPATH , element_address)
    field_address.send_keys("Prushinskih 1/49")
    element_city = "//input[@name = 'city']"
    field_city = driver.find_element(By.XPATH , element_city)
    field_city.send_keys("Minsk")
    element_state = "//input[@name = 'state']"
    field_state = driver.find_element(By.XPATH , element_state)
    field_state.send_keys("USA")
    element_post = "//input[@name = 'postalCode']"
    field_post = driver.find_element(By.XPATH , element_post)
    field_post.send_keys("220112")
    element_country = "//select[@name = 'country']"
    field_country = driver.find_element(By.XPATH , element_country)
    field_country.click()

    element_dropdown = "//option[@value = 'BELARUS']"
    field_dropdown  =  driver.find_element(By.XPATH , element_dropdown)

    field_dropdown.click()

    element_userName = "//input[@name = 'email']"
    field_userName = driver.find_element(By.XPATH , element_userName)
    field_userName.send_keys("admin")
    element_password = "//input[@name = 'password']"
    field_password = driver.find_element(By.XPATH , element_password)
    field_password.send_keys("1234")
    element_confirmPassword = "//input[@name = 'confirmPassword']"
    field_confirmPassword = driver.find_element(By.XPATH , element_confirmPassword)
    field_confirmPassword.send_keys("1234")

    element_buttonSubmit = "//input[@name = 'submit']"
    buttonSubmit = driver.find_element(By.XPATH , element_buttonSubmit)
    buttonSubmit.click()

    name_user = driver.find_element(By.XPATH , "//font[@size= '2']").text
    user_name = driver.find_element(By.XPATH , "//p[3]/font[@size='2']").text

    assert  driver.current_url == "https://demo.guru99.com/test/newtours/register_sucess.php"
    assert "Stanislau Laptsionak" in name_user
    assert "admin" in user_name


