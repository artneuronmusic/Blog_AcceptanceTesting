from behave import *
from selenium import webdriver
from Tests.Acceptance.Page_Model.home_model import HomePage
from Tests.Acceptance.Page_Model.blog_model import BlogModel
from Tests.Acceptance.Page_Model.new_post_model import NewPostPage


use_step_matcher('re')  #to collect scenario from naviation feature


@given("I am on the home page")
def step_impl(context):
    context.driver = webdriver.Chrome()
    home_page = HomePage(context.driver)
    #context.browser.get("http://127.0.0.1:5000")
    context.driver.get(home_page._url)




@given("I am on the blog page")
def step_impl(context):
    context.driver = webdriver.Chrome()
    page = BlogModel(context.driver)
    #context.browser.get("http://127.0.0.1:5000/blog")
    context.driver.get(page._url)


@given("I am on the new post page")
def step_impl(context):
    context.driver = webdriver.Chrome()
    page = NewPostPage(context.driver)
    #context.browser.get("http://127.0.0.1:5000/blog")
    context.driver.get(page._url)



@then("I am on the blog page")
def step_impl(context):
    expected_url = BlogModel(context.driver)._url

    assert context.driver.current_url == expected_url

@then("I am on homepage")
def step_impl(context):
    expected_url = HomePage(context.driver)._url

    assert context.driver.current_url == expected_url





