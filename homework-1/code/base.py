import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException
from ui.locators import base_locators

CLICK_RETRY = 3

class BaseCase:
    driver = None
    config = None

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config):
        self.driver = driver
        self.config = config

    @pytest.fixture()
    def login(self, user_creds):
        login = user_creds.get('login')
        psw = user_creds.get('psw')
        self.click(base_locators.LOGIN_LOCATOR)
        self.fill_input(base_locators.EMAIL_LOCATOR, login)
        self.fill_input(base_locators.PSW_LOCATOR, psw)
        self.click(base_locators.BUTTON_LOCATOR)

    def find(self, locator, timeout = None):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def wait(self, timeout = None):
        if timeout == None:
            timeout = 5
        return WebDriverWait(self.driver, timeout = timeout)

    def fill_input(self, locator, query):
        field = self.find(locator)
        field.clear()
        field.send_keys(query)
    
    def get_data(self, locator):
        field = self.find(locator)
        return field.get_attribute('value')
       
    def check_visibility(self, locator, timeout=None):
        return self.wait(timeout).until(EC.visibility_of_element_located(locator)).is_displayed()

    def check_spinner_removing(self, locator, timeout=None):
        return self.wait(timeout).until(EC.invisibility_of_element_located(locator))

    def click(self, locator, timeout = None):
        for i in range(CLICK_RETRY):
            try:
                element = self.find(locator, timeout=timeout)
                element = self.wait(timeout).until(EC.element_to_be_clickable(locator))
                element.click()
                return
            except StaleElementReferenceException:
                if i == CLICK_RETRY - 1:
                    raise
