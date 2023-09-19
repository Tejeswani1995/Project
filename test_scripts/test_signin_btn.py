import pytest
from src_code.register_page import Register
from src_code.sign_in import SignIn
from inclusive_function.configure import Config
from inclusive_function.examination import Examination
from time import sleep


@pytest.mark.usefixtures("launch_browser","logger")
@pytest.mark.parametrize("username, password",Config.CREDENTIAL)
class TestSignInBtn:

    def test_signinbtn(self, username, password, logger):
        logger.debug("testing signin btn")
        obj = SignIn(self.driver, username, password)
        obj.cookies_btn(Config.COOKIES)
        obj.profile_btn()
        obj.sign_up_link()
        obj.sign_in_btn()
        obj.email_txt()
        obj.continue_btn()
        obj.pwd_txt()
        obj.sign_in_for_product_btn()
        result = obj.check_page(Examination.RESULT_AFTER_SIGN_IN)
        assert result, "page not load"


