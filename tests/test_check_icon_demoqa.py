from pages.demoqa import DemoQa


def test_icon_exist(browser):

    demo_page = DemoQa(browser)  # создание объекта класса DemoQa

    demo_page.visit()  # вызов метода перехода на страницу
    assert demo_page.icon.exist()  # было assert demo_page.exist_icon() # проверка наличия через вызов exist_icon()
    demo_page.icon.click()  # было demo_page.click_on_the_icon()  # вызов метода клика по локатору
    assert demo_page.equal_url()  # проверка URL через вызов метода equal_url()
