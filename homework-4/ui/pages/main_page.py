from ui.pages.base_page import BasePage
from ui.locators.locators_marussia import MainPageLocators

class MainPage(BasePage):
    locators = MainPageLocators()

    def wait_for_loading(self):
        self.find(self.locators.SUGGEST_QUESTION)

    def click_on_keyboard(self):
        self.click_for_android(self.locators.KEYBOARD_BUTTON)
        
    def click_on_menu(self):
        self.click_for_android(self.locators.MENU_BUTTON)

    def input_searchfield(self, req):
        self.find(self.locators.REQUEST_FIELD).send_keys(req)
        self.driver.hide_keyboard()

    def check_visibility_of_keyboard(self):
        return self.check_visibility(self.locators.KEYBOARD_BUTTON)
        
    def enter_request(self):
        self.click_for_android(self.locators.INPUT_BUTTON)
    
    def click_on_suggest(self):
        self.swipe_to_element(self.locators.SUGGEST_POPULATION, self.locators.SUGGEST_LIST)
        self.click_for_android(self.locators.SUGGEST_POPULATION)

    def check_text_in_textbox(self, expected_value) -> bool:
        text = self.find(self.locators.TEXTFIELD).text
        return expected_value in text        

    def check_title_text(self, expected_value) -> bool:
        text = self.find(self.locators.POPULATION_FACT).text
        return text == expected_value
    
    def check_result(self, expected_value) -> bool:
        res = self.find(self.locators.RESULT_DIALOG).text
        return res == expected_value
    
    def check_player_title(self, expected_value) -> bool:
        res = self.find(self.locators.PLAYER_TITLE).text
        return res == expected_value
       
    def change_waitForIdleTimeout(self):
        self.driver.update_settings({
            "waitForIdleTimeout": 100
        })    