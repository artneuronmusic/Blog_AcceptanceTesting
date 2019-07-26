from behave import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from Tests.Acceptance.Locators.blog_locators import BlogLocators


use_step_matcher("re")

@step("I wait for the posts to load")
def step_impl(context):

    WebDriverWait(context.driver, 5).until(
        expected_conditions.visibility_of_element_located(BlogLocators.post_section)
    )



