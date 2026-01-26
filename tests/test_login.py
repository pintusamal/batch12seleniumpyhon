import time

import pytest

from Pages.login_page import LoginPage

class TestLogin:

    @pytest.mark.usefixtures('lunch_the_application')
    def test_validate_login_functionality(self):
        login_page = LoginPage(self.driver)
        login_page.enter_username()
        login_page.enter_password()
        login_page.click_on_submit()
        time.sleep(5)