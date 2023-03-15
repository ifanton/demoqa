# from selenium.webdriver.common.by import By
from pages.demoqa import DemoQa


def test_icon_exist(browser):
    # browser.get("https://demoqa.com/")
    # icon = browser.find_element(By.CSS_SELECTOR, '#app > header > a')
    # if icon is None:
    #     print('Элемент не найден')
    # else:
    #     print('Элемент найден')
    demo_page = DemoQa(browser)  # создание объекта класса DemoQa

    demo_page.visit()  # вызов метода перехода на страницу
    demo_page.click_on_the_icon()  # вызов метода клика по локатору
    assert demo_page.equal_url()  # проверка URL через вызов метода equal_url()
    assert demo_page.exist_icon()  # проверка наличия эл-та через вызов метода exist_icon()
