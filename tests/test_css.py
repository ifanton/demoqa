import allure

from pages.text_box_page import TextBoxPage


@allure.title('tests_check_css')
@allure.story('Проверка CSS селекторов и их свойств')
def test_text_box_submit(browser):
    text_box_page = TextBoxPage(browser)

    text_box_page.visit()
    assert text_box_page.btn_submit.check_css('color', 'rgba(255, 255, 255, 1)')
    assert text_box_page.btn_submit.check_css('backgroundColor', 'rgba(0, 123, 255, 1)')
    assert text_box_page.btn_submit.check_css('borderColor', 'rgb(0, 123, 255)')
