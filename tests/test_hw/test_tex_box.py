import time

from pages.text_box_page import TextBox


def test_text_box(browser):
    text_box_page = TextBox(browser)
    text_box_page.visit()

    text_box_page.full_name.send_keys('tester')
    text_box_page.current_address.send_keys('test1')
    text_box_page.btn_submit.click()

    assert text_box_page.border_name.get_text() == 'Name:'+'tester'
    assert text_box_page.border_address.get_text() == 'Current Address :'+'test1'





