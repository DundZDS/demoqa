import time

from pages.browser_tab import BrowserTab
from pages.links_page import LinksPage


def test_window_tab(browser):
    links_page = LinksPage(browser)
    links_page.visit()


    links_page.btn_home.exist()
    assert links_page.btn_home.get_text() == 'Home'

    assert links_page.btn_home.get_dom_attribute('href') == 'https://demoqa.com'

    assert len(browser.window_handles) ==1
    links_page.btn_home.click()
    time.sleep(2)
    assert len(browser.window_handles) == 2



