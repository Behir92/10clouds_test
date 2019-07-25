from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

from .Base.BasePageObject import BasePageObject


class TenCloudsCaseStudiesPage(BasePageObject):
    def __init__(self, driver):
        super().__init__(driver)

    def get_all_cases(self):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(ec.presence_of_all_elements_located((By.XPATH, '//*[@class="tenc-case-studies--simple__item-app-name"]')))

    def get_all_case_names(self):
        all_cases = self.get_all_cases()
        return [case.get_attribute('innerText') for case in all_cases]
