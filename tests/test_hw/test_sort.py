import time
import pytest
from components.components import WebElement
from pages.webtables import WebTablesPage

@pytest.mark.parametrize("column_header",["FirstName","Last Name","Age","Email","Salary","Department"])
def test_sort(browser, column_header):
    table_page = WebTablesPage(browser)
    table_page.visit()

    column_element = table_page.column_table.find_column_element(column_header)
    column_element.click()
    time.sleep(3)
    assert table_page.column_table.get_dom_attribute('class') == 'rt-resizable-header-content'

@pytest.mark.parametrize("column_header", ["First Name", "Last Name", "Age", "Email", "Salary", "Department"])

def test_sort(browser, column_header):
    page = WebTablesPage(browser)
    page.visit()

    initial_class = page.get_column_header_class(column_header)
    page.click_on_column_header(column_header)
    new_class = page.get_column_header_class(column_header)

    assert initial_class != new_class, f"Сортировка по {column_header} не изменила класс элемента."




