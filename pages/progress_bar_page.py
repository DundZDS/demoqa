from pages.base_page import BasePage
from components.components import WebElement


class ProgressBarPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/progress-bar'
        super().__init__(driver, self.base_url)
        self.btn_start_stop = WebElement(driver, '#startStopButton')
        self.btn_reset = WebElement(driver, '#resetButton')
        self.bar = WebElement(driver,'.progress-bar')