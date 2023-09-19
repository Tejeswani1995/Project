from time import sleep
from inclusive_function.generic_action import GenericActions
from src_code.my_sony import MySony


class Register(MySony,GenericActions):

    sign_in_btn_locator = ("xpath", '//button[contains(.,"Sign-in")]')
    email_locator = ("id", "input-sign-in-id")
    continue_locator = ("id", 'button-sign-in')
    pwd_locator = ("name", "current-password")
    sign_in_locator = ("id", "signin-password-button")

    def __init__(self, driver, log):

        self.driver = driver
        super().__init__(driver, log)
        GenericActions.__init__(self, driver)



    def sign_in_btn(self):
        try:
            self.click_on_element(self.__class__.sign_in_btn_locator)
            return True
        except Exception:
            self.log.info("sign in btn in register page failed")
            return False


    def email_txt(self, username):
        try:
            self.enter_text(self.__class__.email_locator, value=username)
            return True
        except Exception:
            self.log.info("email text failed")
            return False


    def continue_btn(self):
        try:
            sleep(3)
            self.click_on_element(self.__class__.continue_locator)
            return True
        except Exception:
            self.log.info("continue btn fail")
            return False


    def pwd_txt(self, password):
        try:
            self.enter_text(self.__class__.pwd_locator, value=password)
            return True
        except Exception:
            self.log.info("password text failed")
            return False


    def sign_in_for_product_btn(self):
        sleep(3)
        try:
            self.click_on_element(self.__class__.sign_in_locator)
            return True
        except Exception:
            self.log.info("sign in btn failed")
            return False


    def check_page(self, title):
        try:
            self.check_title(title)
            return True
        except Exception:
            self.log.info("page not load")
            return False









