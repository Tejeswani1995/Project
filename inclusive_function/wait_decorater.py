from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait(func):
    def wrapper(*args, **kwargs):

        instance, locator = args

        obj = WebDriverWait(instance.driver, timeout=30)
        webelement = obj.until(EC.visibility_of_element_located(locator), message="element is not visible")

        if webelement.is_enabled():
            return func(*args, **kwargs)

        return False

    return wrapper


