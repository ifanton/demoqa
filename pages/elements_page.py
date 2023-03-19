from components.components import WebElement
from pages.base_page import BasePage


class ElementsPage(BasePage):

    def __init__(self, driver, text=''):
        self.base_url = 'https://demoqa.com/elements'
        self.text = text
        super().__init__(driver, self.base_url)

        self.text_area = WebElement(driver, locator='div.col-12.mt-4.col-md-6',
                                    text='Please select an item from left to start practice.')

    # def equal_url(self): перенесли в класс BasePage
