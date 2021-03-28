import pytest
from base import BaseCase
from ui.locators import base_locators

class TestOne(BaseCase):
    @pytest.mark.UI
    def test_login(self):
        self.login()
        assert self.driver.current_url == 'https://target.my.com/dashboard'
    
    @pytest.mark.UI
    def test_logout(self):
        self.login()
        self.check_spinner_removing(base_locators.SPINNER_LOCATOR)
        self.click(base_locators.MENU_LOCATOR)
        self.click(base_locators.EXIT_LOCATOR)
        self.check_spinner_removing(base_locators.SPINNER_LOCATOR)
        assert self.driver.current_url == 'https://target.my.com/'

    @pytest.mark.UI
    def test_edit_info(self):
        self.login()
        self.click(base_locators.PROFILE_LOCATOR)
        self.fill_input(base_locators.FIO_INPUT_LOCATOR, 'wqeqe')
        self.fill_input(base_locators.PHONE_INPUT_LOCATOR, 'wqeqe')
        self.fill_input(base_locators.EMAIL_INPUT_LOCATOR, 'wqeqe@wqeqe.wq')
        self.click(base_locators.SAVE_LOCATOR)
        result = self.check_visibility(base_locators.SUCCESS_MSG_LOCATOR)
        assert result == True
     
     
    @pytest.mark.parametrize(
        'links',
        [
            pytest.param('billing'),
            pytest.param('statistics')
        ]
    )
    @pytest.mark.UI
    def test_links(self, links):
        self.login()
        generated_locator = (
            base_locators.TEMPLATE_LOCATOR[0],
            base_locators.TEMPLATE_LOCATOR[1].format(links))
        self.click(generated_locator)
        result = self.driver.current_url.find(links)
        assert result != '-1'