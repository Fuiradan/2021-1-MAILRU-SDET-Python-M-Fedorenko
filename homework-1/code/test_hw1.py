import pytest
from base import BaseCase
from ui.locators import base_locators

class TestOne(BaseCase):
    @pytest.mark.UI
    def test_login(self, login):
        assert self.driver.current_url == 'https://target.my.com/dashboard'
    
    @pytest.mark.UI
    def test_logout(self, login):
        self.check_spinner_removing(base_locators.SPINNER_LOCATOR)
        self.click(base_locators.MENU_LOCATOR)
        self.click(base_locators.EXIT_LOCATOR)
        self.check_spinner_removing(base_locators.SPINNER_LOCATOR)
        assert self.driver.current_url == 'https://target.my.com/'

    @pytest.mark.UI
    def test_edit_info(self, login):
        test_data = dict(fio='test_fio', phone='test_number', email='dsf@fasd.io')
        self.click(base_locators.PROFILE_LOCATOR)
        self.fill_input(base_locators.FIO_INPUT_LOCATOR, test_data.get('fio'))
        self.fill_input(base_locators.PHONE_INPUT_LOCATOR,test_data.get('phone'))
        self.fill_input(base_locators.EMAIL_INPUT_LOCATOR, test_data.get('email'))
        self.click(base_locators.SAVE_LOCATOR)
        self.driver.refresh()
        real_data = dict(
            fio = self.get_data(base_locators.FIO_INPUT_LOCATOR),
            phone = self.get_data(base_locators.PHONE_INPUT_LOCATOR),
            email = self.get_data(base_locators.EMAIL_INPUT_LOCATOR)
        )
        assert real_data == test_data
     
    @pytest.mark.parametrize(
        'links',
        [
            pytest.param('billing'),
            pytest.param('statistics')
        ]
    )
    @pytest.mark.UI
    def test_links(self, login, links):
        generated_locator = (
            base_locators.TEMPLATE_LOCATOR[0],
            base_locators.TEMPLATE_LOCATOR[1].format(links))
        self.click(generated_locator)
        result = self.driver.current_url.find(links)
        assert result != '-1'