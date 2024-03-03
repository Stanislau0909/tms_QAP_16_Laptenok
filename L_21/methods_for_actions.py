from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os as os
from selenium.webdriver.common.by import By
import conftest

class Differents_methods:

    def __init__(self,driver,url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)


    def click_on(self, locator):
        self.driver.find_element(*locator).click()


    def force_click(self,locator):
        elements = self.driver.find_elements(*locator)
        if elements:
            element = elements[0]
            self.driver.execute_script("arguments[0].click()", element)
        else:
            print("No elements found for given locator.")

    def click_enter_with_keyboard(self,locator):
        self.driver.find_element(*locator).send_keys(Keys.ENTER)

    def double_click(self,locator):
        my_element = self.driver.find_element(*locator)
        webdriver.ActionChains(self.driver).double_click(my_element).perform()

    def click_right(self,locator):
        element = self.driver.find_element(*locator)
        webdriver.ActionChains(self.driver).context_click(element).perform()

    def enter_data(self,locator,data):
        self.driver.find_element(*locator).send_keys(data)

    def clear_text(self,locator):
        self.driver.find_element(*locator).clear()

    def create_new_tab(self):
        self.driver.switch_to.new_window("tab")

    def create_new_window(self):
        self.driver.switch_to.new_window("window")

    def explicit_wait_to_be_clickable_with_click(self,locator,timeout=5):
        return wait(self.driver,timeout).until(EC.element_to_be_clickable(locator)).click()

    def explicit_wait_to_be_clickable(self,locator,timeout=20):
        return wait(self.driver,timeout).until(EC.element_to_be_clickable(locator))

    def upload_file(self, locator, file):
        self.driver.find_element(*locator).send_keys(f"{os.getcwd()}{file}")







 # check = Wait(driver,5).until(EC.element_to_be_clickable((By.XPATH,"//span[@class= 't-h--28 t-wt--medium t-v--text']"))).find_element(By.XPATH,"//span[@class= 't-h--28 t-wt--medium t-v--text']" ).text