import time

from pages.accordian_page import AccordianPage
from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage


def test_seo(browser):
    demo_page = DemoQa(browser)
    elements_page = ElementsPage(browser)
    accordian_page = AccordianPage(browser)

    demo_page.visit()
    assert browser.title == demo_page.pageData['title']
    time.sleep(2)
    elements_page.visit()
    assert browser.title == elements_page.pageData['title']
    time.sleep(2)
    accordian_page.visit()
    assert browser.title == accordian_page.pageData['title']
