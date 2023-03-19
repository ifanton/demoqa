from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage


def test_go_to_page(browser):

    demo_page = DemoQa(browser)
    elements_page = ElementsPage(browser)

    demo_page.visit()
    assert demo_page.icon.exist()  # было assert demo_page.exist_icon()
    demo_page.btn_elements.click()  # было demo_page.click_on_the_btn_elements()
    assert elements_page.equal_url()
