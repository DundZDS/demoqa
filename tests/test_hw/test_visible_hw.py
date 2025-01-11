from pages.accordian import Accordian
import time

def text_visible_accordian(browser):
    accordian_page = Accordian(browser)
    accordian_page.visit()
    assert accordian_page.section_content.visible()
    accordian_page.section_heading.click()
    time.sleep(2)
    assert not accordian_page.section_content.visible()




