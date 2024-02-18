from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def element_is_visable(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elemets_are_visible(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def elemets_is_present(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def elemets_are_present(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def text_to_be(self,locator ,text, timeout=5):
        return Wait(self.driver,timeout).until(EC.text_to_be_present_in_element(locator,text))

    def text_to_be777(self,locator ,text, timeout=5):
        return Wait(self.driver,timeout).until(EC.text_to_be_present_in_element_value(locator,text))



    def wait_for(self, locator, timeout=10):
        try:
            element = Wait(self.driver, timeout).until(
                EC.visibility_of_element_located((By.XPATH, locator))
            )
            return element
        except TimeoutException:
            assert False, f"Element {locator} does not find"



    def wait_and_click(self,locator,timeout=10):
        try:
            element = Wait(self.driver,timeout).until(
                EC.element_to_be_clickable((By.XPATH,locator))
            )
            element.click()
            return element
        except TimeoutException:
            assert False, f'Element {locator} does not find'