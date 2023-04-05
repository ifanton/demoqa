from components.components import WebElement
from pages.base_page import BasePage


class DroppablePage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/droppable'
        super().__init__(driver, self.base_url)
        self.pageData = {
            'title': 'DEMOQA'
        }

        self.draggable_element = WebElement(driver, locator='#draggable')
        self.droppable_element = WebElement(driver, locator='#droppable')
