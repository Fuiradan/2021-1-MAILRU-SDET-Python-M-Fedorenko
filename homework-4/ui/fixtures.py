import pytest
from appium import webdriver
from ui.pages.base_page import BasePage
from ui.pages.main_page import MainPage
from ui.pages.settings_page import SettingsPage
from ui.pages.news_source_page import NewsSourcePage
from ui.capability import capability_select
from ui.pages.app_info_page import AppInfoPage



@pytest.fixture
def base_page(driver, config):
    return BasePage(driver=driver, config=config)

@pytest.fixture
def main_page(driver, config):
    return MainPage(driver=driver, config=config)

@pytest.fixture
def settings_page(driver, config):
    return SettingsPage(driver=driver, config=config)

@pytest.fixture
def news_source_page(driver, config):
    return NewsSourcePage(driver=driver, config=config)

@pytest.fixture
def app_info_page(driver, config):
    return AppInfoPage(driver=driver, config=config)

@pytest.fixture(scope='function')
def driver(config):
    appium_url = config['appium']
    desired_caps = capability_select()
    driver = webdriver.Remote(appium_url, desired_capabilities=desired_caps)
    yield driver
    driver.quit()