import pytest
from _pytest.fixtures import FixtureRequest

from ui.pages.base_page import BasePage
from ui.pages.main_page import MainPage
from ui.pages.settings_page import SettingsPage
from ui.pages.news_source_page import NewsSourcePage
from ui.pages.app_info_page import AppInfoPage


class BaseCase:

    @pytest.fixture(scope='function', autouse = True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config

        self.base_page: BasePage = request.getfixturevalue('base_page')
        self.main_page: MainPage = request.getfixturevalue('main_page')
        self.settings_page: SettingsPage = request.getfixturevalue('settings_page')
        self.news_source_page: NewsSourcePage = request.getfixturevalue('news_source_page')
        self.app_info_page: AppInfoPage = request.getfixturevalue('app_info_page')
    
    def choose_vesti_fm(self):
        self.main_page.click_on_menu()
        self.settings_page.click_on_news_source()
        self.news_source_page.choose_source()
        return self.news_source_page.check_mark_in_source()
    
    def return_to_main_screen(self):
        while not self.main_page.check_visibility_of_keyboard():
            self.driver.back()
            
    def check_vestifm(self):
        self.main_page.click_on_keyboard()
        self.main_page.change_waitForIdleTimeout()
        self.main_page.input_searchfield("News")
        self.main_page.enter_request()
        return self.main_page.check_player_title("Вести ФМ")