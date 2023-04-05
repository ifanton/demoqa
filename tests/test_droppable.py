import time

import allure

from pages.droppable_page import DroppablePage
from selenium.webdriver import ActionChains  # импорт библиотеки для выполнения low level interactions


@allure.title('test_drag_n_drop')
@allure.story('Проверка drug`n`drop')
def test_drag_n_drop(browser):
    droppable_page = DroppablePage(browser)
    action_chains = ActionChains(browser)   # создание объекта для выполнения действия drug`n`drop

    droppable_page.visit()
    action_chains.drag_and_drop(
        droppable_page.draggable_element.find_element(),  # element
        droppable_page.droppable_element.find_element()   # target
    ).perform()
    assert droppable_page.droppable_element.check_css('backgroundColor', 'steelblue')
    action_chains.drag_and_drop_by_offset(droppable_page.draggable_element.find_element(), -150, 0).perform()
    time.sleep(1)
    assert droppable_page.droppable_element.check_css('backgroundColor', 'steelblue')
    time.sleep(1)
