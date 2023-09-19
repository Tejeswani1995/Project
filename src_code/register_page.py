from inclusive_function.generic_action import GenericActions
from src_code.my_sony import MySony

class Register(MySony,GenericActions):

    create_account_btn_locator = ("xpath", '//span[.="Create Account"]')
    sign_in_btn_locator = ("xpath", '//button[contains(.,"Sign-in")]')
    create_account_pop_up_locator = ("class name", "modal-content")
    terms_conditions_locators = ("xpath", '(//label[contains(.,"terms of service")])[2]')
    proceed_create_acc_locator = ("xpath", '//button[contains(.,"create account")]')


    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)
        GenericActions.__init__(self, driver)

    def create_account_btn(self):
        self.click_on_element(self.__class__.create_account_btn_locator)

    def sign_in_btn(self):
        self.click_on_element(self.__class__.sign_in_btn_locator)

    def updates_checkbox(self,*args):
        if isinstance(args[0],tuple):
            for option in args[0]:
                self.click_on_element(("xpath", f'//label[contains(.,"{option}")]'))
        else:
            pass

    def policy_checkbox(self):
        self.click_on_element(self.__class__.terms_conditions_locators)

    def proceed_to_create_account_btn(self,*args):
        self.updates_checkbox(*args)
        self.click_on_element(self.__class__.proceed_create_acc_locator)


    def check_element(self, locator):
        try:
            result = self.search_element(locator)
            return result
        except Exception:
            return False


    def check_page(self, title):
        try:
            return self.check_title(title)
        except Exception:
            return False





