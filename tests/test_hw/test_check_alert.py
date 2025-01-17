from pages.alerts_page import AlertsPage
from tests.test_hw.conftest import browser
import time

def test_check_alert(browser):
    alerts_page = AlertsPage(browser)
    alerts_page.visit()

    assert not alerts_page.alert()

    alerts_page.timerAlertButton.click()
    time.sleep(6)
    assert alerts_page.alert()
    alerts_page.alert().accept()