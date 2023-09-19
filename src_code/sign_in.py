from time import sleep
from src_code.register_page import Register
from inclusive_function.generic_action import GenericActions
from src_code.register_page import MySony

class SignIn(Register,MySony,GenericActions):

    email_locator = ("id", "input-sign-in-id")
    continue_locator = ("id", 'button-sign-in')
    pwd_locator = ("name", "current-password")
    sign_in_locator = ("id", "signin-password-button")

    def __init__(self, driver, username, pwd):
        self.driver = driver
        super().__init__(driver)
        MySony.__init__(self, driver)
        GenericActions.__init__(self, driver)
        self.username = username
        self.pwd = pwd


    def email_txt(self):
        try:
            self.enter_text(self.__class__.email_locator,value=self.username)
        except Exception:
            pass



    def continue_btn(self):
        sleep(3)
        try:
            self.click_on_element(self.__class__.continue_locator)
        except Exception:
            pass


    def pwd_txt(self):
        try:
            self.enter_text(self.__class__.pwd_locator, value=self.pwd)
        except Exception:
            pass

    def sign_in_for_product_btn(self):
        sleep(5)
        try:
            self.click_on_element(self.__class__.sign_in_locator)
        except Exception:
            pass

    def check_page(self, title):

        try:
            return self.check_title(title)

        except Exception:
            return False


