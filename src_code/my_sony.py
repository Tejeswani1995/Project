from inclusive_function.generic_action import GenericActions


class MySony(GenericActions):

    cookies_accept_locator = ("class name", "button_accept")
    my_sony_icon_locator = ("xpath", '//span[contains(.,"My Sony")]')
    sign_in_link_locator = ("xpath", '//div[contains(@class,"SignUp ")]')


    def __init__(self, driver,log):
        self.driver = driver
        super().__init__(driver)
        self.log = log


    def cookies_btn(self):
        try:
            self.click_on_element(self.__class__.cookies_accept_locator)
            return True
        except Exception:
            self.log.info("cookies failed")
            return False

    def profile_btn(self):
        try:
            self.click_on_element(self.__class__.my_sony_icon_locator)
            return True
        except Exception:
            self.log.info("profile btn failed")
            return False


    def sign_up_link(self):
        try:
            self.click_on_element(self.__class__.sign_in_link_locator)
            return True
        except Exception:
            self.log.info("sign up link failed")
            return False


