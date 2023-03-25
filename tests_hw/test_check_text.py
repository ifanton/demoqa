from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage


def test_check_text(browser):
    demo_page = DemoQa(browser)
    elements_page = ElementsPage(browser)

    demo_page.visit()
    demo_page.footer.get_text()
    assert demo_page.footer.equal_text()

    demo_page.btn_elements.click()
    assert elements_page.text_Please.equal_text()


def test_page_elements(browser):
    elements_page = ElementsPage(browser)

    elements_page.visit()
    assert elements_page.text_Elements.equal_text()

    assert elements_page.icon.exist()
    assert elements_page.btn_sidebar_first.exist()
    assert elements_page.btn_sidebar_first_textbox.exist()
