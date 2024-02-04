import pytest
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def test_locators(driver):
    driver.get("https://www.bbc.com/")
    logo = (driver.find_element(By.XPATH, "//div[@class='orb-nav-section orb-nav-blocks']")) # 1 element
    assert logo
    sign_in = (driver.find_element(By.XPATH, "//span[@id='idcta-username']"))                # 2 element
    assert sign_in
    text = "Home"                                                                            # 3 element
    assert driver.find_element(By.LINK_TEXT, text)
    text = "Sport"                                                                           # 4 element
    assert driver.find_element(By.LINK_TEXT, text)
    text = "Reel"                                                                            # 5 element
    assert driver.find_element(By.LINK_TEXT, text)
    text = "Travel"                                                                          # 6 element
    assert driver.find_element(By.LINK_TEXT, text)
    class_name = "orbit-header-more"                                                         # 7 element
    assert driver.find_element(By.CLASS_NAME, class_name)
    banner = driver.find_element(By.XPATH , "(//div[@class='responsive-image'])[1]")         # 8 element
    assert banner
    text_banner = driver.find_element(By.XPATH,"(//a[@class='media__link'])[8]")             # 9 element
    assert text_banner
    block_news = "a.module__title__link.tag.tag--news"                                       # 10 element
    assert driver.find_element(By.CSS_SELECTOR, block_news)




