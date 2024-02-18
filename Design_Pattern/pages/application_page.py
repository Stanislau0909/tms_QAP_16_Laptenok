import time
from faker import Faker

from Design_Pattern.pages.base_page import BasePage
from Design_Pattern.Locators.applitation_locators import ApplicationPageLocators as Applocators


class Applicationpage(BasePage):
    def create_app_VT(self):
        faker = Faker("ru_RU")
        vin = faker.bothify(text='???##############').upper()
        milage = faker.bothify(text='#####')
        model = faker.bothify(text='#####')
        theme = "ТЕСТОВАЯ ЗАЯВКА В РАБОТУ НЕ БРАТЬ!"
        description = "ТЕСТОВАЯ ЗАЯВКА , ЗДЕСЬ ТЕКСТ ДЛЯ ТЕСТА, Камаз-54901 он же К5 магистральный седельный тягач, со своим эксклюзивным мотором P6. " \
                      "На правах флагманской модели КАМАЗ, с полным соответствием всеми принятым стандартам автомобилестроения. В этой теме обсуждаем эту модель, " \
                      "рассказываем о вопросах эксплуатации, ремонта и обслуживания. Пишите, свой отзыв о этой модели. Самые интересные отзывы отправим на завод и обязательно пришлем ответ!"

        self.element_is_visable(Applocators.BUTTON_FOR_CREATE_APP).click()
        self.element_is_visable(Applocators.LIST_TYPES_APPS).click()
        self.element_is_visable(Applocators.REPAIR_APP).click()
        self.element_is_visable(Applocators.SUBMIT_CHOSEN_CATEGORY_APP).click()
        self.element_is_visable(Applocators.LIST_FAMILY).click()
        self.element_is_visable(Applocators.FAMILY_K3).click()
        self.element_is_visable(Applocators.VIN).send_keys(vin)
        self.element_is_visable(Applocators.MILEAGE).send_keys(milage)
        self.element_is_visable(Applocators.MODEL).send_keys(model)
        self.element_is_visable(Applocators.LIST_DEFECT_NODE).click()
        self.element_is_visable(Applocators.DEFECT_NODE_AUTO).click()
        self.element_is_visable(Applocators.THEME).send_keys(faker.text())
        self.element_is_visable(Applocators.DESCRIPTION).send_keys(description)
        self.element_is_visable(Applocators.CREATE_BUTTON).click()

    def check_status_app(self):
        self.name_status1 = "Отправлена"
        self.name_status2 = "Назначена"
        self.name_status3 = "В работе СДС"
        self.name_status4 = "Ожидает ответа АЗК"
        self.name_status5 = "Конструктор"
        self.name_status6 = "Ожидает закрытия"
        self.name_status7 = "Завершена"
        self.name_status8 = "Успешно завершена"
        time.sleep(1)
        self.cheking_status_app = self.element_is_visable(Applocators.CHECK_STATUS_APP).text
        return self.cheking_status_app

    def notification_about_successufully_create_app(self):
        self.notification = "Заявка успешно создана"
        self.success = self.element_is_visable(Applocators.SUCCESSFULY_CREATE_APP).text
        return self.success

    def assign_app_for_specialist(self):
        my_specialist = "Лаптёнок(вт)"
        self.element_is_visable(Applocators.MENU_NEAR_THEME).click()
        self.element_is_visable(Applocators.BUTTON_ASSIGN).click()
        self.element_is_visable(Applocators.LIST_SPECIALIST).click()
        self.element_is_visable(Applocators.IMPUT_FOR_ENTER_DATA_SPEIALIST).click()
        time.sleep(1)
        self.element_is_visable(Applocators.IMPUT_FOR_ENTER_DATA_SPEIALIST).send_keys(my_specialist)
        time.sleep(1)
        self.element_is_visable(Applocators.FIRST_FOUND_SPECIALIST_IN_LIST).click()
        self.element_is_visable(Applocators.SUBMIT_ASSIGN).click()





    def check_implementer_in_app(self):
        self.my_specialist = "Лаптёнок(вт) С. В."
        self.cheking_spec = self.element_is_visable(Applocators.CHECK_IMPLEMENTER_IN_APP).text
        time.sleep(1)
        return self.cheking_spec


    def open_app(self):
        self.element_is_visable(Applocators.OPEN_FIRST_APP_TABLE).click()














