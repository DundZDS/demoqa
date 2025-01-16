from components.components import WebElement
from pages.base_page import BasePage

from pages.herokuapp_base_page import KoupPage


class KoupAdd(BasePage):
    def __init__(self,driver):
        self.base_url = 'http://the-internet.herokuapp.com/add_remove_elements/'
        super().__init__(driver, self.base_url)
        self.btn_add_element = WebElement(driver, '.example > button')
        self.btn_delete = WebElement(driver, 'button.added-manually')



