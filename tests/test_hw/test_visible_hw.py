from components.components import WebElement
from conftest import browser
from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage
from pages.accordian import Accordian
import time

def text_visible_accordian(browser):
    accordian = Accordian(browser)
    accordian.visit()
    assert accordian.section_content.visible()
    accordian.section_heading.click()
    time.sleep(2)
    assert not accordian.section_content.visible()




