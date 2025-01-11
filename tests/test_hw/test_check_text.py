from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage


def test_check_text(browser):
    demo_qa_page = DemoQa(browser)
    elements_page = ElementsPage(browser)
    demo_qa_page.visit()
    assert demo_qa_page.footer.get_text() == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.', 'Текст не соответствует'
    demo_qa_page.btn_elements.click()
    assert elements_page.middle.get_text() == 'Please select an item from left to start practice.', 'Текст не соответствует'