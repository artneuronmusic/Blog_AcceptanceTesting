from behave import *
import time
from Tests.Acceptance.Page_Model.base_model import BasePage
from Tests.Acceptance.Page_Model.new_post_model import NewPostPage



use_step_matcher('re')

@when('I click on the link "(.*)"') #use the regular expression liek format to replace variable
def step_impl(context, link_text):   #(.*) is equal to link_id =>parameter
    #link = context.driver.find_element_by_id(link_text)
    #link.click()

    page = BasePage(context.driver)
    links = page._navigation

    valid_links = [l for l in links if l.text == link_text]
    if len(valid_links) > 0:
        valid_links[0].click()
    else:
        raise RuntimeError


@when('I enter "(.*)" in the "(.*)" field')
def step_impl(context, content, field_name):

    page = NewPostPage(context.driver)
    page._form_field((field_name).send_keys(content))

@when("I click on the submit button")
def step_impl(context):
    page = NewPostPage(context.driver)
    page._submit_button.click()










