from ui.pages.base_page import BasePage
from ui.locators.locators_marussia import NewsSourceLocators

class NewsSourcePage(BasePage):
    locators = NewsSourceLocators()

    def choose_source(self):
        self.click_for_android(self.locators.VESTIFM_BUTTON)

    def check_mark_in_source(self) -> bool:
        checkmark_parent = self.find(self.locators.CHECKMARK_PARENT)
        source_name = checkmark_parent.find_element(self.locators.TEXTVIEW[0], self.locators.TEXTVIEW[1]).text
        return "Вести FM" == source_name