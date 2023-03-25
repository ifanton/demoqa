import time
from pages.accordian_page import AccordianPage


def test_visible_accordian(browser):
    accordian_page = AccordianPage(browser)

    accordian_page.visit()
    assert accordian_page.text_What_Lorem.visible()
    accordian_page.header_What_Lorem.click()
    time.sleep(2)
    assert not accordian_page.text_What_Lorem.visible()


def test_visible_accordian_default(browser):
    accordian_page = AccordianPage(browser)

    accordian_page.visit()
    assert not accordian_page.text_Where1_Lorem.visible()
    assert not accordian_page.text_Where2_Lorem.visible()
    assert not accordian_page.text_Why_Lorem.visible()
