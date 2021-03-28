from selenium.webdriver.common.by import By

LOGIN_LOCATOR = (By.CLASS_NAME, 'responseHead-module-button-1BMAy4')
EMAIL_LOCATOR = (By.NAME, 'email')
PSW_LOCATOR = (By.NAME, 'password')
BUTTON_LOCATOR = (By.CLASS_NAME, 'authForm-module-button-2G6lZu')
MENU_LOCATOR = (By.CLASS_NAME, 'right-module-rightButton-39YRvc')
EXIT_LOCATOR = (By.XPATH, '//a[@href="/logout"]')
PROFILE_LOCATOR = (By.XPATH, '//a[@href="/profile"]')
FIO_INPUT_LOCATOR = (By.XPATH, '//div[@data-name="fio"]//input')
PHONE_INPUT_LOCATOR = (By.XPATH, '//div[@data-name="phone"]//input')
EMAIL_INPUT_LOCATOR = (By.XPATH, '//div[contains(@class,"additional-email")]//input')
SAVE_LOCATOR = (By.XPATH, '//div[text()="Сохранить"]')
SUCCESS_MSG_LOCATOR = (By.XPATH, '//div[@data-class-name="SuccessView"]')
TEMPLATE_LOCATOR = (By.XPATH, '//a[@href="/{}"]')
SPINNER_LOCATOR = (By.XPATH, '//div[contains(@class,"spinner")]')