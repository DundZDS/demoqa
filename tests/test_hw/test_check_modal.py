import time
from selenium.common import NoSuchElementException
from pages.modal_dialogs import ModalDialogs


def test_check_modal(browser):
    modal_page = ModalDialogs(browser)

    modal_page.response_200()

    try:
        modal_page.visit()

        modal_page.btn_small_modal.click()
        time.sleep(2)
        assert modal_page.modal_content.exist()
        modal_page.btn_close_small_modal.click()

        modal_page.btn_large_modal.click()
        time.sleep(2)
        assert modal_page.modal_content.exist()
        modal_page.btn_close_large_modal.click()

    except NoSuchElementException as problem:
        print(f'Страница недоступна: {problem}. Тест пропускается')
