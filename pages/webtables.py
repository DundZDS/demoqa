from websocket import debug

from components.components import WebElement
from pages.base_page import BasePage


class WebTablesPage(BasePage):

    def __init__(self,driver):
        self.base_url = 'https://demoqa.com/webtables'
        super().__init__(driver, self.base_url)
        self.no_data = WebElement(driver, 'div.rt-noData')
        self.btn_delete_row = WebElement(driver, ' #delete-record')
        self.btn_add = WebElement(driver, ' #addNewRecordButton')
        self.btn_edit = WebElement(driver, '#edit-record')
        self.modal_form = WebElement(driver,'.modal-content')
        self.first_name = WebElement(driver,'#firstName')
        self.last_name = WebElement(driver,'#lastName')
        self.user_email = WebElement(driver, '#userEmail')
        self.last_name = WebElement(driver, '#lastName')
        self.age = WebElement(driver, '#age')
        self.salary = WebElement(driver,'#salary')
        self.department = WebElement(driver,'#department')
        self.btn_submit = WebElement(driver, '#submit')

        self.btn_edit_4 = WebElement(driver,'#edit-record-4 > svg:nth-child(1) > path:nth-child(1)')
        self.btn_del_4 = WebElement (driver, '#delete-record-4 > svg:nth-child(1) > path:nth-child(1)')
        self.rows = WebElement(driver,'.select-wrap > select')
        self.btn_previous = WebElement(driver,'.-previous')
        self.btn_next = WebElement(driver, '.-next')
        self.table_page = WebElement(driver, '.-pageJump > input')
        self.total_table_page = WebElement(driver,".-totalPages")
