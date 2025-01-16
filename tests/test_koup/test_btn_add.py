from components.components import WebElement
from pages.herokuapp_base_page import KoupPage
from pages.koup_add_remove_elements_page import KoupAdd
import time


def test_koup_btn_add(browser):
    koup_page = KoupPage(browser)
    koup_add = KoupAdd(browser)
    koup_page.visit()

    assert koup_page.link_add.get_text() == 'Add/Remove Elements'
    koup_page.link_add.click()
    assert koup_add.equal_url()

    assert koup_add.btn_add_element.get_text() == 'Add Element'

    assert koup_add.btn_add_element.get_dom_attribute('onclick') == 'addElement()'


    for i in range(4):
        koup_add.btn_add_element.click()

    time.sleep(2)

    assert koup_add.btn_delete.check_count_elements(4)

    for element in koup_add.btn_delete.find_elements():
        assert 'Delete' == element.text

    while koup_add.btn_delete.exist():
        koup_add.btn_delete.click()

    assert not koup_add.btn_delete.exist()
