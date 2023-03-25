from pages.base_page import BasePage
from components.components import WebElement


class AccordianPage(BasePage):

    def __init__(self, driver, text=''):
        self.base_url = 'https://demoqa.com/accordian'
        self.text = text
        super().__init__(driver, self.base_url)

        self.text_What_Lorem = WebElement(driver, locator='#section1Content > p')
        self.header_What_Lorem = WebElement(driver, locator='#section1Heading')
        self.text_Where1_Lorem = WebElement(driver, locator='#section2Content > p:nth-child(1)')
        self.text_Where2_Lorem = WebElement(driver, locator='#section2Content > p:nth-child(2)')
        self.text_Why_Lorem = WebElement(driver, locator='#section3Content > p')
