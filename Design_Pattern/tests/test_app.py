import time

from Design_Pattern.pages.application_page import Applicationpage as App
from Design_Pattern.data_test.data import Data
from Design_Pattern.ENV import ENV
from Design_Pattern.pages.auth_page import AuthPage as Auth


class TestApppage:

    def test_create_applicationVT(self,driver):
        app = App(driver,ENV)
        data = Data(driver,ENV)
        app.open()
        data.data_diagnost()
        app.create_app_VT()
        assert app.notification_about_successufully_create_app() == app.notification

    def test_assign_app(self,driver):
        app = App(driver, ENV)
        data = Data(driver, ENV)
        auth = Auth(driver, ENV)
        auth.log_out()
        data.data_specVT()
        app.open_app()
        app.assign_app_for_specialist()
        assert app.check_status_app() == app.name_status2







