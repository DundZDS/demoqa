from components.components import WebElement
from pages.base_page import BasePage


class TextBox(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/text-box'
        super().__init__(driver, self.base_url)
        self.full_name = WebElement(driver, '#userName')
        self.user_email = WebElement(driver,'#userEmail')
        self.current_address = WebElement(driver, '#currentAddress')
        self.permanent_address = WebElement(driver, '#permanentAddress')
        self.btn_submit = WebElement(driver,'#submit')
        self.border_name = WebElement(driver, '#name')
        self.border_address = WebElement (driver, 'p.mb-1:nth-child(2)')
