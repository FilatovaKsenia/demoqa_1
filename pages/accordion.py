from conftest import browser
from pages.base_page import BasePage
from components.components import WebElement

class Accordion(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/accordian'
        super().__init__(driver, self.base_url)

        self.content_1 = WebElement(driver, '#section1Content > p')
        self.first_btn = WebElement(driver, '#section1Heading')
        self.content_2 = WebElement(driver, '#section2Content > p:nth-child(1)')
        self.content_2_2 = WebElement(driver, '#section2Content > p:nth-child(2)')
        self.content_3 = WebElement(driver, '#section3Content > p')