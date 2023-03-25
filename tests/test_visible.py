import time

from pages.elements_page import ElementsPage


def test_visible_btn_sidebar(browser):
    elements_page = ElementsPage(browser)

    elements_page.visit()
    # elements_page.btn_sidebar_first.click()
    # time.sleep(3)
    # assert elements_page.btn_sidebar_first_textbox.exist()  # assert ОБЯЗАТЕЛЬНО - проверка наличия элемента: T/F
    assert elements_page.btn_sidebar_first_textbox.visible()  # assert ОБЯЗАТЕЛЬНО - проверка наличия элемента: T/F


def test_not_visible_btn_sidebar(browser):
    elements_page = ElementsPage(browser)

    elements_page.visit()
    assert elements_page.btn_sidebar_first_check_box.visible()
    elements_page.btn_sidebar_first.click()
    time.sleep(2)
    assert not elements_page.btn_sidebar_first_check_box.visible()
