from pages.demoqa import Demoqa

def test_icon_exist(browser):
    demo_qa_page = Demoqa(browser)
    demo_qa_page.visit()
    demo_qa_page.icon.click()
    assert demo_qa_page.equal_url()
    assert demo_qa_page.icon.exist()

