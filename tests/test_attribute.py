import time

from pages.text_box_page import TextBoxPage


def test_placeholder(browser):
    text_box_page = TextBoxPage(browser)

    text_box_page.visit()
    assert text_box_page.full_name.get_dom_attribute('placeholder') == 'Full Name'
    assert text_box_page.full_name.get_dom_attribute('autocomplete') == 'off'
    assert text_box_page.full_name.get_dom_attribute('type') == 'text'
