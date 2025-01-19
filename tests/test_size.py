import time
from pages.demoqa import Demoqa

def test_size(browser):
    demo_qa_page = Demoqa(browser)

    demo_qa_page.visit()
    browser.set_window_size(1000, 300)
    time.sleep(2)
    browser.set_window_size(1000, 1000)