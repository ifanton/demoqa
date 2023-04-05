from components.components import WebElement
from pages.base_page import BasePage


class BrowserTabPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/browser-windows'
        super().__init__(driver, self.base_url)
        self.pageData = {
            'title': 'DEMOQA'
        }

        self.btn_new_tab = WebElement(driver, locator='#tabButton')
        self.btn_new_window = WebElement(driver, locator='#windowButton')
