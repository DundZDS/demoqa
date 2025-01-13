from pages.modal_dialogs import ModalDialogs



def test_modal_elements(browser):
    page_modal_dialogs = ModalDialogs(browser)
    page_modal_dialogs.visit()

    assert page_modal_dialogs.btn_second_menu.check_count_elements(count=5)

def test_navigation_modal(browser):
    page_modal_dialogs = ModalDialogs(browser)
    page_modal_dialogs.visit()
    page_modal_dialogs.refresh()
    page_modal_dialogs.icon_base_page.click()
    browser.back()
    browser.set_window_size(900,400)
    browser.forward()
    page_modal_dialogs.equal_url()
    assert browser.title == 'DEMOQA'
    browser.set_window_size(1000, 1000)
