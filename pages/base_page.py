class BasePage:

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    def visit(self):  # метод перехода на страницу
        return self.driver.get(self.base_url)  # возвращает переход через .get()

    # def find_element(self, locator): перенесли в components.py

    def get_url(self):  # возвращает текущий URL
        return self.driver.current_url

    def equal_url(self):  # сравнивает текущий URL с заданной строкой
        if self.get_url() == self.base_url:
            return True
        else:
            return False
