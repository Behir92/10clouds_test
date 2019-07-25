class BasePageObject:
    def __init__(self, driver):
        self.__driver = driver

    @property
    def driver(self):
        return self.__driver
