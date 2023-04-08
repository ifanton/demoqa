import allure
import time

from selenium.webdriver.common.by import By

from pages.webtable_page import WebtablePage


@allure.feature('test_webtable_sort')
@allure.story('Сортировка таблицы по каждому столбцу')
@allure.severity(allure.severity_level.NORMAL)
def test_webtable_sort(browser):
    webtable_page = WebtablePage(browser)
    text_sort = ['First Name', 'Last Name', 'Age', 'Email', 'Salary', 'Department']

    webtable_page.visit()
    for text in text_sort:
        browser.find_element(By.XPATH, f"//*[.='{text}']").click()
        assert browser.find_element(By.XPATH, f"//*[.='{text}']").get_dom_attribute('class') == 'rt-th rt-resizable' \
                                                                                                '-header -sort-asc ' \
                                                                                                '-cursor-pointer'
        browser.find_element(By.XPATH, f"//*[.='{text}']").click()
        assert browser.find_element(By.XPATH, f"//*[.='{text}']").get_dom_attribute('class') == 'rt-th rt-resizable' \
                                                                                                '-header -sort-desc ' \
                                                                                                '-cursor-pointer'
        time.sleep(1)
