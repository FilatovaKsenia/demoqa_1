from pages.allerts import Alerts
import time

def test_check_alert(browser):
    alert_page = Alerts(browser)

    alert_page.visit()
    alert_page.timerAlertButton.click()
    time.sleep(5)
    assert alert_page.alert()
