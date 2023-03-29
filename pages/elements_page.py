from components.components import WebElement
from pages.base_page import BasePage


class ElementsPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/elements'
        super().__init__(driver, self.base_url)
        self.pageData = {
            'title': 'DEMOQA'
        }

        self.text_Please = WebElement(driver, locator='div.col-12.mt-4.col-md-6',
                                      text='Please select an item from left to start practice.')
        self.text_Elements = WebElement(driver, locator='div.pattern-backgound.playgound-header > div',
                                        text='Elements')
        self.icon = WebElement(driver, locator='#app > header > a')
        self.btn_sidebar_first = WebElement(driver, locator='div:nth-child(1) > span > div')
        self.btn_sidebar_first_textbox = WebElement(driver, locator='div:nth-child(1) > div > ul > #item-0 > span')
        self.btn_sidebar_first_check_box = WebElement(driver, locator='div:nth-child(1) > div > ul > #item-1')
        self.btns_first_menu = WebElement(driver, locator='div:nth-child(1) > div > ul > li')
