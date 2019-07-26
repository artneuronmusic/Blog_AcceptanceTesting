from behave import *
from selenium import webdriver
#from selenium.webdriver.common.by import By
from Tests.Acceptance.Page_Model.base_model import BasePage
#from Tests.Acceptance.Page_Model.home_model import HomePage
from Tests.Acceptance.Page_Model.blog_model import BlogModel


use_step_matcher('re')


@then("There is a title shown on the page")
def step_impl(context):
    title_tag = BasePage(context.driver)
    title_tag._title
    #BlogPageLocators.title is a tuple
    #the * can deconstruct the tuple into individual argument

    assert title_tag._title.is_displayed()
    #because of the use of @property in base_model, so the title_tag does not need bracket anymore


@step('The title tag has content "(.*)"')
def step_impl(context, content):
    #title_tag = context.browser.find_element(By.TAG_NAME, "h1")
    title_tag = BasePage(context.driver)

    assert title_tag._title.text == content


@then("I can see there is a posts section on the page")
def step_impl(context):
    page = BlogModel(context.driver)
    assert page._post_section.is_displayed()


@then('I can see there is a post with title "(.*)" in the posts section')
def step_impl(context, title):
    page = BlogModel(context.driver)
    post_with_content = [post for post in page._post_list if post.text == title]
    assert len(post_with_content) > 0
    assert all( post.is_displayed() for post in page._post_list)


