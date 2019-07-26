from Tests.Acceptance.Page_Model.base_model import BasePage
#from Tests.Acceptance.Page_Model.home_model import HomePage
from Tests.Acceptance.Locators.blog_locators import BlogLocators

class BlogModel(BasePage):

    #def __init__(self, driver):
     #   self.driver = driver

    @property
    def _url(self):
        return super(BlogModel, self)._url + "/blog"

    @property
    def _home_link(self):
        return self.driver.find_element(*BlogLocators.home_link)

    @property
    def _create_post(self):
        return self.driver.find_element(*BlogLocators.add_post)

    @property
    def _show_post(self):
        return self.driver.find_element(*BlogLocators.post_section)

    @property
    def _post_list(self):
        return self.driver.find_elements(*BlogLocators.post)

    @property
    def _post_section(self):
        return self.driver.find_element(*BlogLocators.post_section)



