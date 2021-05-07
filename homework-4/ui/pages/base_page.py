from selenium.common.exceptions import StaleElementReferenceException, TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction

CLICK_RETRY = 3
BASE_TIMEOUT = 5


class BasePage(object):
    def __init__(self, driver, config):
        self.driver = driver
        self.config = config
    
    def click_for_android(self, locator, timeout=None):
        for i in range(CLICK_RETRY):
            try:
                element = self.find(locator, timeout=timeout)
                element = self.wait(timeout).until(EC.element_to_be_clickable(locator))
                element.click()
                return
            except StaleElementReferenceException:
                if i == CLICK_RETRY - 1:
                    raise
    
    def wait(self, timeout=None):
        if timeout is None:
            timeout = 5
        return WebDriverWait(self.driver, timeout=timeout)

    def find(self, locator, timeout=None):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def swipe_menu_right(self, loc_swipe_menu, swipetime=200):
        action = TouchAction(self.driver)
        menu = self.find(loc_swipe_menu)
        dimension = menu.size
        location = menu.location
        start_x = int(dimension['width'] * 0.9)
        end_x = int(dimension['width'] * 0.7)
        y = int(location['y'])
        action. \
            press(x=start_x, y=y). \
            wait(ms=swipetime). \
            move_to(x=end_x, y=y). \
            release(). \
            perform()

    def swipe_to_element(self, locator, loc_swipe_menu=None, max_swipes=5):
        already_swiped = 0
        while len(self.driver.find_elements(*locator)) == 0:
            if already_swiped > max_swipes:
                raise TimeoutException("Error with lo, please check function")
            if loc_swipe_menu != None:
                self.swipe_menu_right(loc_swipe_menu)
            else:
                self.swipe_down()
            already_swiped += 1

    def swipe_down(self, swipetime=200):
        action = TouchAction(self.driver)
        dimension = self.driver.get_window_size()
        x = int(dimension['width'] / 2)
        start_y = int(dimension['height'] * 0.8)
        end_y = int(dimension['height'] * 0.5)
        action. \
            press(x=x, y=start_y). \
            wait(ms=swipetime). \
            move_to(x=x, y=end_y). \
            release(). \
            perform()

    def check_visibility(self, locator):
        try:
            self.driver.find_element(locator[0], locator[1])
            return True
        except NoSuchElementException:
            return False
