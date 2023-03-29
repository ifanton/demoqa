from components.components import WebElement
from pages.base_page import BasePage


class ModalDialogs(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)
        self.pageData = {
            'title': 'DEMOQA'
        }

        self.btn_light = WebElement(driver, locator='div:nth-child(3) > div > ul > li')
        self.icon = WebElement(driver, locator='#app > header > a')
