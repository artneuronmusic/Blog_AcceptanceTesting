from selenium.webdriver.common.by import By

class BasePageLocators:

    title = By.TAG_NAME, "h1"

    nav_links = By.CLASS_NAME, "nav-link"