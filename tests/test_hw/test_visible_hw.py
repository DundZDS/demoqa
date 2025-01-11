import time
from pages.accordion import Accordion

def test_visible_accordian(browser):
    accordian_page = Accordion(browser)
    accordian_page.visit()
    assert accordian_page.section_1_content.visible()
    accordian_page.section_heading.click()
    time.sleep(2)
    assert not (accordian_page.section_1_content.visible())

def test_visible_accordion_default(browser):
    accordian_page = Accordion(browser)
    accordian_page.visit()
    assert not accordian_page.section_2_content_child_1.visible()
    assert not accordian_page.section_2_content_child_2.visible()
    assert not accordian_page.section_3_content.visible()





