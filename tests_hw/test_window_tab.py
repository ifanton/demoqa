import allure

from pages.links_page import LinksPage


@allure.feature('test_link_opens_in_new_tab')
@allure.story('Проверка открытия новой вкладки по клику на ссылку')
@allure.severity(allure.severity_level.NORMAL)
def test_link_opens_in_new_tab(browser):
    links_page = LinksPage(browser)

    links_page.visit()
    assert links_page.link_home.get_text() == 'Home'
    assert links_page.link_home.get_dom_attribute('href') == 'https://demoqa.com'
    links_page.link_home.click()
    assert len(browser.window_handles) == 2
    browser.switch_to.window(browser.window_handles[1])
    assert browser.current_url == 'https://demoqa.com/'
