import allure

from selenium.webdriver import Keys

from pages.webtable_page import WebtablePage


@allure.feature('webtable')
@allure.story('Добавление, изменение и удаление записей в таблице - позитивный')
@allure.severity(allure.severity_level.NORMAL)
def test_webtable_actions(browser):
    webtable_page = WebtablePage(browser)

    webtable_page.visit()
    webtable_page.btn_add.click()
    assert webtable_page.modal_window.visible()
    webtable_page.modal_window_btn_submit.click()
    assert webtable_page.modal_window_user_form.get_dom_attribute('class') == 'was-validated'
    webtable_page.modal_window_first_name.send_keys('Anton')
    webtable_page.modal_window_last_name.send_keys('Panteleev')
    webtable_page.modal_window_email.send_keys('email@email.com')
    webtable_page.modal_window_age.send_keys('37')
    webtable_page.modal_window_salary.send_keys('100000')
    webtable_page.modal_window_department.send_keys('QA')
    webtable_page.modal_window_btn_submit.click()
    assert not webtable_page.modal_window.exist()
    assert webtable_page.table_pencil_4.exist()
    webtable_page.table_pencil_4.click_force()
    assert webtable_page.modal_window.visible()
    webtable_page.modal_window_first_name.clear()
    webtable_page.modal_window_first_name.send_keys('Anthony')
    webtable_page.modal_window_btn_submit.click()
    assert webtable_page.table_name.get_text() == 'Anthony'
    webtable_page.table_bin_4.click_force()
    assert not webtable_page.table_bin_4.exist()
    assert not webtable_page.table_no_elements.exist()  # убеждаемся, что в таблице есть записи
    while webtable_page.table_bin.exist():  # цикл удаляет записи по неуникальному локатору пока они есть
        webtable_page.table_bin.click_force()
    assert webtable_page.table_no_elements.visible()  # убеждаемся, что в таблице нет записей (No rows found)


@allure.feature('webtable')
@allure.story('Навигация в таблице - позитивный')
@allure.severity(allure.severity_level.NORMAL)
def test_webtable_navigation(browser):
    webtable_page = WebtablePage(browser)

    webtable_page.visit()
    webtable_page.table_size_selector.scroll_to_element()
    webtable_page.table_size_selector.click_force()
    webtable_page.table_size_selector.send_keys(Keys.ARROW_UP)
    webtable_page.table_size_selector.send_keys(Keys.ENTER)
    webtable_page.table_nav_btn_previous.click()
    webtable_page.table_nav_btn_next.click()
    assert webtable_page.table_nav_page_index.get_dom_attribute('value') == '1'
    assert webtable_page.table_nav_btn_previous.get_dom_attribute('disabled')
    # когда кнопка неактивна, у нее имеется атрибут disabled="",
    # когда кнопка активна, данного атрибута нет совсем
    assert webtable_page.table_nav_btn_next.get_dom_attribute('disabled')
    for i in range(1, 4):
        webtable_page.btn_add.click()
        webtable_page.modal_window_first_name.send_keys('Anton')
        webtable_page.modal_window_last_name.send_keys('Panteleev')
        webtable_page.modal_window_email.send_keys('email@email.com')
        webtable_page.modal_window_age.send_keys('37')
        webtable_page.modal_window_salary.send_keys('100000')
        webtable_page.modal_window_department.send_keys('QA')
        webtable_page.modal_window_btn_submit.click()
    assert webtable_page.table_nav_page_counter.get_text() == '2'
    assert not webtable_page.table_nav_btn_next.get_dom_attribute('disabled')
    webtable_page.table_nav_btn_next.click()
    assert webtable_page.table_nav_page_index.get_dom_attribute('value') == '2'
    webtable_page.table_nav_btn_previous.click()
    assert webtable_page.table_nav_page_index.get_dom_attribute('value') == '1'
