from pages.modal_dialogs import ModalDialogs
import time


def test_small_and_large_buttons(browser):
    modal_dialogs = ModalDialogs(browser)
    modal_dialogs.visit()

    assert modal_dialogs.btn_small_modal.exist()
    assert modal_dialogs.btn_large_modal.exist()
    assert not modal_dialogs.modal_windows.exist()

    modal_dialogs.btn_small_modal.click()
    time.sleep(2)
    assert modal_dialogs.modal_windows.exist()
    assert modal_dialogs.title_small_modal.get_text() == 'Small Modal'
    assert modal_dialogs.btn_close_small_modal.exist()
    modal_dialogs.btn_close_small_modal.click()
    time.sleep(2)
    assert not modal_dialogs.modal_windows.exist()

    modal_dialogs.btn_large_modal.click()
    time.sleep(2)
    assert modal_dialogs.modal_windows.exist()
    assert modal_dialogs.title_large_modal.get_text() == 'Large Modal'
    assert modal_dialogs.btn_close_large_modal.exist()
    modal_dialogs.btn_close_large_modal.click()
    time.sleep(2)
    assert not modal_dialogs.modal_windows.exist()