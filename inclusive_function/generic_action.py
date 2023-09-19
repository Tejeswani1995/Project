from datetime import datetime
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from inclusive_function.configure import Config
from inclusive_function.wait_decorater import wait


class GenericActions():

    def __init__(self, driver):
        self.driver = driver

    @wait
    def enter_text(self, locator, value):
        self.driver.find_element(*locator).send_keys(value)

    @wait
    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()


    def take_screenshot(self):
        dt = datetime.now()
        screenshot_name = f"screenshot_{dt.year}-{dt.month}-{dt.day}--{dt.hour}-{dt.minute}-{dt.second}.png"
        self.driver.save_screenshot(Config.SCREENSHOT_PATH + screenshot_name)


    @wait
    def search_element(self, locator):
        webelement_list = self.driver.find_elements(*locator)
        return webelement_list

    @wait
    def check_link_text(self, locator):
        if "//a" in locator[1]:
            result = self.driver.find_element(*locator).text
            return result
        else:
            pass

    @wait
    def get_all_option_in_dropdown(self,locator):
        list_box = self.driver.find_element(*locator)
        drop_ob = Select(list_box)
        return drop_ob.options


    def check_title(self, expected_title):
        wait = WebDriverWait(self.driver, 30)
        if wait.until(EC.title_is(expected_title)):
            return True
        return False



