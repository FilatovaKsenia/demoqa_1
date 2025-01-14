from pages.demoqa import Demoqa
import time

def test_icon_exist(browser):
    demo_qa_page = Demoqa(browser)
    demo_qa_page.visit()
    demo_qa_page.click_on_the_icon()
    assert demo_qa_page.equal_url()
    assert demo_qa_page.exist_icon()

