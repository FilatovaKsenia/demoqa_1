from pages.accordion import Accordion
import time


def test_visible_accordion(browser):
    accordian_page = Accordion(browser)
    accordian_page.visit()
    assert accordian_page.content_1.visible()
    accordian_page.first_btn.click()
    time.sleep(2)
    assert not accordian_page.first_btn.visible()

def test_visible_accordion_default(browser):
    accordian_page = Accordion(browser)
    accordian_page.visit()
    assert not accordian_page.content_2.visible()
    assert not accordian_page.content_2_2.visible()
    assert not accordian_page.content_3.visible()