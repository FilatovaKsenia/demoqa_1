
from pages.modal_dialogs import ModalDialogs


def test_modal_elements(browser):
    modal_dialog_page = ModalDialogs(browser)
    modal_dialog_page.visit()

    assert modal_dialog_page.btn_submenu.check_count_elements(count=5)

def test_navigation_modal(browser):
    modal_dialog_page = ModalDialogs(browser)
    modal_dialog_page.visit()
    modal_dialog_page.refresh()
    modal_dialog_page.icon.click()
    browser.back()
    browser.set_window_size(900, 400)
    browser.forward()
    modal_dialog_page.equal_url()
    assert browser.title == 'DEMOQA'
    browser.set_window_size(1000, 1000)