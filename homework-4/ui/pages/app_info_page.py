from ui.pages.base_page import BasePage
from ui.locators.locators_marussia import AppInfoLocators

class AppInfoPage(BasePage):
    locators = AppInfoLocators()
    
    def compare_versions(self) -> bool:
        version_string = self.find(self.locators.VERSION_TEXT).text
        version_in_app = version_string.split(' ')[1]
        apk_name = self.driver.session["app"]
        return version_in_app in apk_name

    def check_trademark(self, exp_value) -> bool:
        trademark = self.find(self.locators.TRADEMARK_LOC).text
        return exp_value in trademark
