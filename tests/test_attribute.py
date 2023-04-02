import allure

from pages.text_box_page import TextBoxPage


@allure.feature('check attr')  # указывает к какой фиче или блоку принадлежит тест
@allure.story('Проверка атрибутов поля FULL NAME')  # нужен для описания конкретного теста
@allure.severity(allure.severity_level.BLOCKER)  # это важность тест кейса
def test_attr_exist(browser):
    text_box_page = TextBoxPage(browser)

    text_box_page.visit()
    assert text_box_page.full_name.get_dom_attribute('placeholder') == 'Full Name'
    assert text_box_page.full_name.get_dom_attribute('autocomplete') == 'off'
    assert text_box_page.full_name.get_dom_attribute('type') == 'text'


@allure.feature('check attr')
@allure.story('Проверка упавшего теста')
@allure.severity(allure.severity_level.BLOCKER)
def test_fail():  # Например: проверка заведомо ложного утверждения
    assert 111 == 222
