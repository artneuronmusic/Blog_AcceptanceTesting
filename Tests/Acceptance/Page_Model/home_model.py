from Tests.Acceptance.Locators.home_page_locators import HomePageLocators
from Tests.Acceptance.Page_Model.base_model import BasePage

class HomePage(BasePage):

    @property
    def _url(self):
        return super(HomePage, self)._url + "/"




    @property
    def _blog_link(self):
        return self.driver.find_element(*HomePageLocators.navigation_id)