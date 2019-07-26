from Tests.Acceptance.Page_Model.base_model import BasePage
#from Tests.Acceptance.Page_Model.home_model import HomePage
from Tests.Acceptance.Locators.blog_locators import BlogLocators
from Tests.Acceptance.Locators.new_page_locators import NewPostPageLocators
from selenium.webdriver.common.by import By

class NewPostPage(BasePage):

    #def __init__(self, driver):
     #   self.driver = driver

    @property
    def _url(self):
        return super(NewPostPage, self)._url + "/post"

    @property
    def _return_blog(self):
        return self.driver.find_element(*NewPostPageLocators.return_blog)

    @property
    def _post_form(self):
        return self.driver.find_element(*NewPostPageLocators.post_form)

    @property
    def _form_field(self, name):
        return self._post_form.find_element(By.NAME, name)

    @property
    def _submit_button(self):
        return self.driver.find_element(*NewPostPageLocators.submit)
