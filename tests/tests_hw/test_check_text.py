from pages.demoqa import Demoqa
from pages.elements_page import ElementsPage

def test_check_text_footer(browser):
    demo_qa_page = Demoqa(browser)
    demo_qa_page.visit()
    assert demo_qa_page.footer.get_text() == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'

def test_check_text_center(browser):
    demo_qa_page = Demoqa(browser)
    elements_page = ElementsPage(browser)
    demo_qa_page.visit()
    demo_qa_page.btn_elements.click()
    assert elements_page.center_element.get_text() == 'Please select an item from left to start practice.'