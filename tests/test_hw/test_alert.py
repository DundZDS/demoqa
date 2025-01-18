import time
from pages.alerts_page import AlertsPage

def test_alert(browser):
    alerts_page = AlertsPage(browser)
    alerts_page.visit()

    assert not alerts_page.alert()
    alerts_page.alertButton.click()
    time.sleep(2)
    assert alerts_page.alert()
    alerts_page.alert().accept()

def test_alert_text(browser):
    alerts_page = AlertsPage(browser)
    alerts_page.visit()

    alerts_page.alertButton.click()
    assert alerts_page.alert().text == 'You clicked a button'
    alerts_page.alert().accept()
    assert not alerts_page.alert()

def test_confirm(browser):
    alerts_page = AlertsPage(browser)
    alerts_page.visit()

    alerts_page.confirmButton.click()
    time.sleep(2)
    alerts_page.alert().dismiss()
    assert alerts_page.confirmResult.get_text() == 'You selected Cancel'

def test_prompt(browser):
    alerts_page = AlertsPage(browser)
    name = 'Denis'
    alerts_page.visit()

    alerts_page.promptButton.click()
    time.sleep(2)
    alerts_page.alert().send_keys(name)
    alerts_page.alert().accept()
    assert alerts_page.promptResult.get_text() == f'You entered { name }'
