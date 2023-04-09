import allure
import time

from pages.progress_bar_page import ProgressBarPage


@allure.feature('test_progress_bar')
@allure.story('Запуск прогресс-бара и остановка на конкретном значении')
@allure.severity(allure.severity_level.NORMAL)
def test_progress_bar(browser):
    progress_bar_page = ProgressBarPage(browser)

    progress_bar_page.visit()
    time.sleep(2)
    assert progress_bar_page.btn_start.exist()
    assert progress_bar_page.progress_bar.get_dom_attribute('aria-valuenow') == '0'
    progress_bar_page.btn_start.click()
    while True:
        if progress_bar_page.progress_bar.get_dom_attribute('aria-valuenow') == '51':
            progress_bar_page.btn_start.click()
            break
    # while int(progress_bar_page.progress_bar.get_dom_attribute('aria-valuenow')) < 51:
    #     print()
    # progress_bar_page.btn_start.click()
    assert progress_bar_page.progress_bar.get_dom_attribute('aria-valuenow') == '51'
    time.sleep(3)
