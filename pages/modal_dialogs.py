from pages.base_page import BasePage
from components.components import WebElement


class ModalDialogs(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)
        self.btn_second_menu = WebElement(driver, 'div:nth-child(3) > div > ul > li')
        self.icon_base_page = WebElement(driver, '#app > header:nth-child(1) > a:nth-child(1) > img:nth-child(1)')


