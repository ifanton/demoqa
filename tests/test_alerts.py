import time

import allure

from pages.alerts_page import AlertsPage


@allure.title('tests_for_alert_confirm_prompt')
@allure.story('Проверка alert')
def test_alerts(browser):
    alerts_page = AlertsPage(browser)

    alerts_page.visit()
    assert not alerts_page.alert()
    alerts_page.btn_alert.click()
    time.sleep(2)
    assert alerts_page.alert()
    alerts_page.alert().accept()  # подтверждение alert
    time.sleep(2)


@allure.title('tests_for_alert_confirm_prompt')
@allure.story('Проверка текста в окне alert')
def test_alert_text(browser):
    alert_page = AlertsPage(browser)

    alert_page.visit()
    alert_page.btn_alert.click()
    time.sleep(2)
    assert alert_page.alert().text == 'You clicked a button'
    alert_page.alert().accept()
    assert not alert_page.alert()
    time.sleep(2)


@allure.title('tests_for_alert_confirm_prompt')
@allure.story('Проверка отмены в confirm')
def test_confirm(browser):
    alert_page = AlertsPage(browser)

    alert_page.visit()
    alert_page.btn_alert_confirm.click()
    time.sleep(2)
    alert_page.alert().dismiss()  # отмена alert
    assert alert_page.text_selection_result.get_text() == 'You selected Cancel'
    time.sleep(2)


@allure.title('tests_for_alert_confirm_prompt')
@allure.story('Проверка ввода текста в prompt')
def test_prompt(browser):
    alert_page = AlertsPage(browser)

    alert_page.visit()
    alert_page.btn_alert_prompt.click()
    time.sleep(2)
    alert_page.alert().send_keys('Anton')
    alert_page.alert().accept()
    assert alert_page.text_prompt_result.get_text() == 'You entered Anton'
    time.sleep(2)
