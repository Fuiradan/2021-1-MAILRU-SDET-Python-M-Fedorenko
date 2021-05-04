from appium.webdriver.common.mobileby import MobileBy

class BasePageLocators:
    pass

class MainPageLocators(BasePageLocators):
    KEYBOARD_BUTTON = (MobileBy.ID, 'ru.mail.search.electroscope:id/keyboard')
    MENU_BUTTON = (MobileBy.ID, 'ru.mail.search.electroscope:id/assistant_menu_bottom')
    REQUEST_FIELD = (MobileBy.ID, 'ru.mail.search.electroscope:id/input_text')
    INPUT_BUTTON = (MobileBy.ID,'ru.mail.search.electroscope:id/text_input_action')
    TEXTFIELD = (MobileBy.ID, 'ru.mail.search.electroscope:id/item_dialog_fact_card_content_text')
    SUGGEST_LIST = (MobileBy.ID, 'ru.mail.search.electroscope:id/suggests_list')
    SUGGEST_QUESTION = (MobileBy.XPATH, '//android.widget.TextView[contains(@text,"Что ты умеешь?")]')
    SUGGEST_POPULATION = (MobileBy.XPATH, '//android.widget.TextView[contains(@text,"численность населения россии")]')
    POPULATION_FACT = (MobileBy.XPATH, '//android.widget.FrameLayout[3]//android.widget.TextView[contains(@resource-id,"card_title")]')
    RESULT_DIALOG = (MobileBy.XPATH, '//androidx.recyclerview.widget.RecyclerView/android.widget.TextView[contains(@resource-id,"dialog_item")]')
    PLAYER_TITLE = (MobileBy.ID, "ru.mail.search.electroscope:id/player_track_name")

class SettingsPageLocators(BasePageLocators):
    NSOURCE_BUTTON = (MobileBy.ID, 'ru.mail.search.electroscope:id/user_settings_field_news_sources')
    APPINFO_BUTTON = (MobileBy.ID, 'ru.mail.search.electroscope:id/user_settings_about')

class NewsSourceLocators(BasePageLocators):
    VESTIFM_BUTTON = (MobileBy.XPATH, '//android.widget.TextView[contains(@text, "Вести FM")]')
    CHECKMARK_PARENT = (MobileBy.XPATH, '//android.widget.ImageView[contains(@resource-id, "item_selected")]/parent::*')
    TEXTVIEW = (MobileBy.CLASS_NAME,"android.widget.TextView")

class AppInfoLocators(BasePageLocators):
    VERSION_TEXT = (MobileBy.ID, 'ru.mail.search.electroscope:id/about_version')
    TRADEMARK_LOC = (MobileBy.ID, 'ru.mail.search.electroscope:id/about_copyright')

    