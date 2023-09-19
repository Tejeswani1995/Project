from inclusive_function.generic_action import GenericActions


class MySony(GenericActions):

    cookies_manage_locator = ("class name", "button_manage")
    cookies_accept_locator = ("class name", "button_accept")
    my_sony_icon_locator = ("xpath", '//span[contains(.,"My Sony")]')
    sign_in_link_locator = ("xpath", '//div[contains(@class,"SignUp ")]')


    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)


    def cookies_btn(self, condition):
        if condition == "manage":
            self.click_on_element(self.__class__.cookies_manage_locator)

        elif condition == "accept":
            self.click_on_element(self.__class__.cookies_accept_locator)

        else:
            pass

    def profile_btn(self):
        self.click_on_element(self.__class__.my_sony_icon_locator)


    def sign_up_link(self):
        self.click_on_element(self.__class__.sign_in_link_locator)


    def check_page(self, title):
        return self.check_title(title)

    def check_element(self, locator):
        result = self.search_element(locator)
        return result