from components.components import WebElement
from pages.base_page import BasePage


class TextBoxPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/text-box'
        super().__init__(driver, self.base_url)
        self.pageData = {
            'title': 'DEMOQA'
        }

        self.full_name = WebElement(driver, locator='#userName')
