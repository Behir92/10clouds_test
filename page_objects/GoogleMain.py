from .Base.BasePageObject import BasePageObject
from .Base.PageElements import Button, Input


class GoogleMain(BasePageObject):
    def __init__(self, driver):
        super().__init__(driver)
        self.search_bar = Input(self.driver, '//input[@class="gLFyf gsfi"]')
        self.correct_link = Button(self.driver, '//h3[@class="LC20lb"]')