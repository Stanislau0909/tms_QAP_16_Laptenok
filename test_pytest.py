import time

import pytest
from selenium.webdriver.common.by import By


def check_age(user):
    if user > 18:
        return True
    else:
        return False

@pytest.mark.smoke
@pytest.mark.parametrize('age',[19,100])
def test_positive(age):
    assert check_age(age)


@pytest.mark.negative
@pytest.mark.parametrize(
    'creds',
    [
    pytest.param(('test', 123),id='test,123',),
    pytest.param(("login",'passw123'),id="login,passw123")
    ]
)
def test_invalid_creds(driver,creds):
    login,passw = creds
    driver.get('https://v2.azkts.ru/login/')
    input_login = driver.find_element(By.XPATH, "//input[@type='login']").send_keys(login)
    input_password = driver.find_element(By.XPATH,"//input[@type='password']").send_keys(passw)
    submit_button = driver.find_element(By.XPATH,"//button[@type='submit']").click()
    time.sleep(1)
    notification = driver.find_element(By.XPATH,"//div[@class='notification Danger']").text
    assert "Неверный логин или пароль" == notification


