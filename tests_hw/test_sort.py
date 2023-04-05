import allure
import time
from selenium.webdriver import Keys

from pages.webtable_page import WebtablePage


@allure.feature('test_webtable_sort')
@allure.story('Сортировка таблицы по каждому столбцу')
@allure.severity(allure.severity_level.NORMAL)
def test_webtable_sort(browser):
    webtable_page = WebtablePage(browser)

    webtable_page.visit()
    assert webtable_page.table_header_firstName.get_dom_attribute('class') == 'rt-th rt-resizable-header ' \
                                                                              '-cursor-pointer'  # нет сортировки
    webtable_page.table_header_firstName.click()
    assert webtable_page.table_header_firstName.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-asc ' \
                                                                              '-cursor-pointer'  # по возрастанию
    webtable_page.table_header_firstName.click()
    assert webtable_page.table_header_firstName.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-desc ' \
                                                                              '-cursor-pointer'  # по убыванию
    # и так далее с заголовками каждого столбца
