from .Base.BasePageObject import BasePageObject
from .Base.PageElements import PageElement, Button


class TenCloudsMain(BasePageObject):
    def __init__(self, driver):
        super().__init__(driver)
        self.cases_section = Section(self.driver, '//*[@class="tenc-case-studies--simple"]')


class Section(PageElement):
    def __init__(self, driver, locator_path):
        super().__init__(driver, locator_path)
        self.all_cases_button = Button(self.driver, '//*[@class="tenc-case-studies--simple-more-button"]/a')

