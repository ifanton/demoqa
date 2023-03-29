from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage


def test_navigation(browser):
    demo_page = DemoQa(browser)
    elements_page = ElementsPage(browser)

    demo_page.visit()
    demo_page.btn_elements.click()
    demo_page.refresh()

    browser.refresh()
    browser.back()
    browser.forward()

    assert elements_page.text_Please.equal_text()
