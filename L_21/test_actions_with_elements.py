import os
import time

from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from L_21.methods_for_actions import Differents_methods as B
from L_21.elements_21 import  WebElements as E
import conftest
urlSite = "http://main.azkts.dev.nch.dpkapp.ru/"
path_tofile: str = "/attachments/kamaz_evening.jpg"

class TestActions:

    def test_action_like_just_click(self,driver):
        base = B(driver,urlSite)
        base.open()
        base.click_on(E.BUTTON_ENG)

    def test_force_click(self,driver):
        base = B(driver,urlSite)
        base.force_click(E.BUTTON_RUS)

    def test_enter_data(self,driver):
        base = B(driver, urlSite)
        base.enter_data(E.INPUT_LOGIN,"diagnostqa")
        base.enter_data(E.INPUT_PASSWORD,"524598")


    def test_clear_input(self,driver):
        base = B(driver, urlSite)
        base.clear_text(E.INPUT_LOGIN)

    def test_create_new_tab(self,driver):
        base = B(driver, urlSite)
        base.create_new_tab()
        base.open()


    def test_open_new_tab_and_use_it(self,driver):
        base = B(driver,urlSite)
        tab = driver.window_handles
        driver.switch_to.window(tab[1])
        base.enter_data(E.INPUT_LOGIN, "diagnostqa")
        base.enter_data(E.INPUT_PASSWORD, "524598")
        base.force_click(E.BUTTOM_SUBMIT)
        check = base.explicit_wait_to_be_clickable(E.NAME_MAIN_SCREEN).text
        assert check == "Заявки"
        print(check)

    def test_create_application_upload_attachemts(self,driver):
        base = B(driver, urlSite)
        base.explicit_wait_to_be_clickable_with_click(E.BUTTON_FOR_CREATE_APP)
        base.explicit_wait_to_be_clickable_with_click(E.LIST_TYPES_APPS)
        base.explicit_wait_to_be_clickable_with_click(E.REPAIR_APP)
        base.explicit_wait_to_be_clickable_with_click(E.SUBMIT_CHOSEN_CATEGORY_APP)
        base.explicit_wait_to_be_clickable_with_click(E.LIST_FAMILY)
        base.explicit_wait_to_be_clickable_with_click(E.FAMILY_K3)
        base.enter_data(E.VIN,12345678911234567)
        base.enter_data(E.MILEAGE,80000)
        base.explicit_wait_to_be_clickable_with_click(E.LIST_DEFECT_NODE)
        base.explicit_wait_to_be_clickable_with_click(E.DEFECT_NODE_AUTO)
        base.enter_data(E.MODEL,54901)
        base.enter_data(E.THEME,"Test of application , don't take in work")
        base.enter_data(E.DESCRIPTION,"just test")
        base.upload_file(E.DRAG_AND_DROP,"/attachments/kamaz_evening.jpg")
        base.upload_file(E.DRAG_AND_DROP, "/attachments/kamaz_video.mp4")
        base.explicit_wait_to_be_clickable_with_click(E.CREATE_BUTTON)
        check = base.explicit_wait_to_be_clickable(E.NUMBER_OF_APPLICATION).text
        print(check)

































