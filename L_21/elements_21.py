from selenium.webdriver.common.by import By
from webdriver_manager.core import driver

from L_21.methods_for_actions import Differents_methods

class WebElements:

        #auth
        BUTTON_RUS = (By.XPATH , "//*[text()='Русский']")
        BUTTON_ENG = (By.XPATH , "//*[text()='English']")
        INPUT_LOGIN = (By.XPATH,"//input[@type='login']")
        INPUT_PASSWORD = (By.XPATH,"//input[@type='password']")
        CHECK_BOX = (By.XPATH,"//input[@type='checkbox']")
        FORGOT_PASSWORD =(By.XPATH,"//span[@class='t-pt--15 t-wt--regular t-v--info AuthForm-Title']")
        BUTTOM_SUBMIT =(By.XPATH,"//button[@type='submit']")

        #Application
        NAME_MAIN_SCREEN = (By.XPATH, "//*[text()='Заявки']")

        # Первое модальное окно при создании заявки
        BUTTON_FOR_CREATE_APP = (
        By.XPATH, "//button[@class= 'Button--YUouf accent--3a4zQ md--3cLPB ApplicationsPage-Tools_btn']")
        LIST_TYPES_APPS = (By.XPATH, "//div[@class= 'selector---Eebj md--GBbBs']")
        REPAIR_APP = (By.XPATH, "//div[@class= 'item--AsZ9e md--1_JQH'][1]")
        MECHANIC_APP = (By.XPATH, "//div[@class= 'item--AsZ9e md--1_JQH'][2]")
        FIRMWARE_APP = (By.XPATH, "//div[@class= 'item--AsZ9e md--1_JQH'][3]")
        SUBMIT_CHOSEN_CATEGORY_APP = (By.XPATH, "//button[@class= 'Button--YUouf accent--3a4zQ sm--5RYLw']")

        # Второе модальное окно при создании заявки ВТ
        LIST_FAMILY = (By.XPATH, "//div[@class='selector---Eebj md--GBbBs']")
        FAMILY_K3 = (By.XPATH, "(//div[@class='item--AsZ9e md--1_JQH'])[1]")
        VIN = (By.XPATH, "(//input[@class='input  '])[1]")
        MILEAGE = (By.XPATH, "(//input[@class='input  '])[3]")
        LIST_DEFECT_NODE = (By.XPATH, "(//div[@class='selector---Eebj md--GBbBs'])[2]")
        DEFECT_NODE_AUTO = (By.XPATH, "(//span[@class='label--OKIJs'])[1]")
        MODEL = (By.XPATH, "(//input[@class='input  '])[4]")
        THEME = (By.XPATH, "(//input[@class='input  '])[6]")
        DESCRIPTION = (By.XPATH, "(//input[@type='simple'])[3]")
        CREATE_BUTTON = (By.XPATH, "//button[@class='Button--YUouf accent--3a4zQ sm--5RYLw']")
        DRAG_AND_DROP = (By.XPATH,"//input[@type='file']")

        #auditlog



        #application_into
        NUMBER_OF_APPLICATION = (By.XPATH,"(//span[@class='t-pt--15 t-wt--regular t-v--text MainInfoRAE-InfoItemValue'])[7]")
        #for_explicity_wait
        ATTRIBUTE = 'class'
        text = "Заявки"











