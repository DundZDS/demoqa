import time

from pages.webtables import WebTablesPage
from selenium.webdriver import Keys


def test_del_tables(browser):
    web_tables = WebTablesPage(browser)
    web_tables.visit()

    web_tables.rows.send_keys(Keys.PAGE_UP)
    web_tables.rows.send_keys(Keys.ENTER)

    assert web_tables.btn_previous.checking_for_the_disabled_attribute()
    assert web_tables.btn_next.checking_for_the_disabled_attribute()

    for i in range(3):

        web_tables.btn_add.click()

        web_tables.first_name.send_keys('tester')
        web_tables.last_name.send_keys('testov')
        web_tables.user_email.send_keys('test@test.com')
        web_tables.age.send_keys('30')
        web_tables.salary.send_keys('300000')
        web_tables.department.send_keys('SPb')
        web_tables.btn_submit.click()


    assert web_tables.total_table_page.get_text() == '2'

    web_tables.btn_next.click()
    assert  web_tables.table_page.get_dom_attribute('value') == '2'
    web_tables.btn_previous.click()
    assert web_tables.table_page.get_dom_attribute('value') == '1'










