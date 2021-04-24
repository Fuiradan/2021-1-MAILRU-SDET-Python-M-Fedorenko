import pytest
import time
from base import BaseCase



class TestMarussia(BaseCase):

    @pytest.mark.Android
    def test_Russia(self):
        self.main_page.click_on_keyboard()
        self.main_page.input_searchfield("Russia")
        self.main_page.enter_request()
        assert self.main_page.check_text_in_textbox("Росси́йская Федера́ция") == True
        self.main_page.click_on_suggest()
        assert self.main_page.check_title_text('146 млн.') == True
    
    @pytest.mark.Android
    def test_calculator(self):
        self.main_page.click_on_keyboard()
        self.main_page.input_searchfield("5**2")
        self.main_page.enter_request()
        assert self.main_page.check_result('25') == True

    @pytest.mark.Android
    def test_news(self):
        self.main_page.click_on_menu()
        self.settings_page.click_on_news_source()
        self.news_source_page.choose_source()
        assert self.news_source_page.check_mark_in_source() == True
        self.base_page.press_back_button()
        self.base_page.press_back_button()
        self.main_page.click_on_keyboard()
        self.main_page.change_waitForIdleTimeout()
        self.main_page.input_searchfield("News")
        self.main_page.enter_request()
        assert self.main_page.check_player_title("Вести ФМ") == True

    @pytest.mark.Android
    def test_version(self):
        self.main_page.click_on_menu()
        self.settings_page.click_on_app_info()
        assert self.app_info_page.compare_versions() == True
        assert self.app_info_page.check_trademark('Все права защищены')
        
        


    


        

        
