from Tests.Acceptance.Locators.base_page_locators import BasePageLocators

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @property
    def _url(self):
        return "http://127.0.0.1:5000"

    @property
    def _title(self):
        return self.driver.find_element(*BasePageLocators.title)

    @property
    def _navigation(self):
        return self.driver.find_elements(*BasePageLocators.nav_links)

