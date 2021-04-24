from ui.pages.base_page import BasePage
from ui.locators.locators_marussia import SettingsPageLocators

class SettingsPage(BasePage):
    locators = SettingsPageLocators()

    def click_on_news_source(self):
        self.swipe_to_element(self.locators.NSOURCE_BUTTON)
        self.click_for_android(self.locators.NSOURCE_BUTTON)

    def click_on_app_info(self):
        self.swipe_to_element(self.locators.APPINFO_BUTTON)
        self.click_for_android(self.locators.APPINFO_BUTTON)