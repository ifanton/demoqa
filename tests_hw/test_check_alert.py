import time

import allure

from pages.alerts_page import AlertsPage


@allure.title('tests_check_5sec_alert')
@allure.story('Проверка 5 sec alert')
def tests_check_5sec_alert(browser):
    alerts_page = AlertsPage(browser)

    alerts_page.visit()
    alerts_page.btn_5sec_alert.click()
    assert not alerts_page.alert()
    time.sleep(5)
    assert alerts_page.alert()
    alerts_page.alert().accept()  # подтверждение alert
    time.sleep(2)
