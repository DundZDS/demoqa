from pages.base_page import BasePage
from components.components import WebElement


class Accordian(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/accordian'
        super().__init__(driver, self.base_url)

        self.section_content = WebElement(driver, '#section1Content > p:nth-child(1)')
        self.section_heading = WebElement(driver, '#section1Heading')