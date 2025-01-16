import time

from pages.webtables import WebTablesPage


def test_del_tables(browser):
    web_tables = WebTablesPage(browser)
    web_tables.visit()

    assert not web_tables.no_data.exist()

    while web_tables.btn_delete_row.exist():
        web_tables.btn_delete_row.click()

    time.sleep(2)
    assert web_tables.no_data.exist()

