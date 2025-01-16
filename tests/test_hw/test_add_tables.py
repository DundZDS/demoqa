from pages.webtables import WebTablesPage


def test_del_tables(browser):
    web_tables = WebTablesPage(browser)
    web_tables.visit()

    web_tables.btn_add.click()
    assert web_tables.modal_form.exist()
    web_tables.first_name.send_keys('tester')
    web_tables.last_name.send_keys('testov')
    web_tables.user_email.send_keys('test@test.com')
    web_tables.age.send_keys('30')
    web_tables.salary.send_keys('300000')
    web_tables.department.send_keys('SPb')
    web_tables.btn_submit.click()

    web_tables.btn_edit_4.click()
    web_tables.first_name.clear()
    web_tables.first_name.send_keys('test')
    web_tables.btn_submit.click()


    web_tables.btn_del_4.click()
