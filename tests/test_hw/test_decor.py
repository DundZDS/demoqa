import pytest

from pages.demoqa import DemoQa
from pages.radio_button_page import RadioButtonPage


@pytest.mark.skip
def test_decor_skip(browser):
    page = DemoQa(browser)

    page.visit()
    assert page.h5.check_count_elements(6)

    for element in page.h5.find_elements():
        assert element.text != ''


@pytest.mark.skipif(True, reason='просто пропуск')
def test_decor_skipif(browser):
    page = RadioButtonPage(browser)

    page.visit()
    page.yes.click_force()
    assert page.text.get_text() == 'You have selected Yes'

    page.impressive.click_force()
    assert page.text.get_text() == 'You have selected Impressive'

    assert 'disabled' in page.no.get_dom_attribute('class')
