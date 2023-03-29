import time

from pages.text_box_page import TextBoxPage


def test_clear(browser):
    text_box_page = TextBoxPage(browser)

    text_box_page.visit()
    text_box_page.full_name.send_keys('Hello')
    time.sleep(2)
    text_box_page.full_name.clear()
    time.sleep(2)
    assert text_box_page.full_name.get_text() == ''
