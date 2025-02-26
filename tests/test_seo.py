from pages.demoqa import Demoqa
from pages.accordion import Accordion
from pages.allerts import Alerts
from pages.browser_tab import BrowserTab
import pytest
import time

def test_check_title_demo(browser):
    demo_qa_page = Demoqa(browser)

    demo_qa_page.visit()
    assert browser.title == 'DEMOQA'

@pytest.mark.parametrize("pages", [Accordion, Alerts, Demoqa, BrowserTab])
def test_check_title_all_pages(browser, pages):
    page = pages(browser)

    page.visit()
    time.sleep(2)
    assert page.get_title() == 'DEMOQA'