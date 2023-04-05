import time

from pages.demoqa import DemoQa
from pages.modal_dialogs_page import ModalDialogs


def test_modal_dialogs(browser):
    modal_dialogs_page = ModalDialogs(browser)

    modal_dialogs_page.visit()
    assert modal_dialogs_page.btn_light.check_count_elements(5)


def test_navigation_modal(browser):
    modal_dialogs_page = ModalDialogs(browser)
    demo_page = DemoQa(browser)

    modal_dialogs_page.visit()
    modal_dialogs_page.refresh()
    modal_dialogs_page.icon.click()
    browser.back()
    browser.set_window_size(900, 400)
    browser.forward()
    demo_page.equal_url()
    assert browser.title == demo_page.pageData['title']
    time.sleep(2)
    browser.set_window_size(1000, 1000)
    time.sleep(2)

