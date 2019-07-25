from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class PageElement:
    def __init__(self, driver, locator_path, by=By.XPATH):
        self.__driver = driver
        self.__locator_path = locator_path
        self.__locator = (by, locator_path)

    @property
    def driver(self):
        return self.__driver

    @property
    def locatorPath(self):
        return self.__locator_path

    @property
    def locator(self):
        return self.__locator

    @property
    def webelement(self):
        wait = WebDriverWait(self.driver, 10)
        webelement = wait.until(ec.visibility_of_element_located(self.locator))
        return webelement

    def get_inner_text(self):
        return self.webelement.get_attribute('innerText')

    def is_element_displayed(self):
        return self.webelement.is_displayed()


class Button(PageElement):
    def click_element(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.webelement).click()
        action.perform()


class Input(PageElement):
    def input_text_and_press_enter(self, text):
        action = ActionChains(self.driver)
        action.move_to_element(self.webelement).send_keys(text)
        action.send_keys(Keys.ENTER)
        action.perform()
