import pytest
import time
from base import BaseCase



class TestMarussia(BaseCase):

    @pytest.mark.Android
    def test_Russia(self):
        self.main_page.wait_for_loading()
        self.main_page.click_on_keyboard()
        self.main_page.input_searchfield("Russia")
        self.main_page.enter_request()
        assert self.main_page.check_text_in_textbox("Территория России")
        self.main_page.click_on_suggest()
        assert self.main_page.check_title_text('146 млн.')
    
    @pytest.mark.Android
    def test_calculator(self):
        self.main_page.wait_for_loading()
        self.main_page.click_on_keyboard()
        self.main_page.input_searchfield("5**2")
        self.main_page.enter_request()
        assert self.main_page.check_result('25')

    @pytest.mark.Android
    def test_news(self):
        self.main_page.wait_for_loading()
        assert self.choose_vesti_fm()
        self.return_to_main_screen()
        assert self.check_vestifm()

    @pytest.mark.Android
    def test_version(self):
        self.main_page.wait_for_loading()
        self.main_page.click_on_menu()
        self.settings_page.click_on_app_info()
        assert self.app_info_page.compare_versions()
        assert self.app_info_page.check_trademark('Все права защищены')
        
        


    


        

        
