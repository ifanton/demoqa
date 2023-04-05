import time

import allure

from pages.browser_tab import BrowserTabPage


@allure.title('test_new_tab')
@allure.story('Проверка открытия новой вкладки и обратный переход в первую вкладку')
def test_alerts(browser):
    browser_tab_page = BrowserTabPage(browser)

    browser_tab_page.visit()
    assert len(browser.window_handles) == 1
    browser_tab_page.btn_new_tab.click()
    browser.switch_to.window(browser.window_handles[1])
    time.sleep(2)
    assert browser.current_url == 'https://demoqa.com/sample'
    time.sleep(2)
    assert len(browser.window_handles) == 2
    browser.switch_to.window(browser.window_handles[0])
    assert browser_tab_page.equal_url()
    time.sleep(2)
