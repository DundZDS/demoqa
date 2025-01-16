from selenium.webdriver.common.by import By

from components.components import WebElement
from pages.base_page import BasePage


class KoupPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'http://the-internet.herokuapp.com'
        super().__init__(driver, self.base_url)
        self.btn_add_remove_elements = WebElement(driver, '#content > ul:nth-child(4) > li:nth-child(2) > a:nth-child(1)')
        self.link_add = WebElement(driver, '#content > ul:nth-child(4) > li:nth-child(2) > a:nth-child(1)')

class BasePage:

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    def visit(self):
        return self.driver.get(self.base_url)

    def back(self):
        self.driver.back()

    def forward(self):
        self.driver.forward()

    def refresh(self):
        self.driver.refresh()

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def equal_url(self):
        if self.get_url() == self.base_url:
            return True
        else:
            return False