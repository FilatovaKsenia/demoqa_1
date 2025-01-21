import time
# import allure
from pages.tables import Tables


# def test_tables(browser):
#
#     page_tables = Tables(browser)
#
#     page_tables.visit()
#     assert not page_tables.no_data.exist()
#
#     while page_tables.btn_delete_row.exist():
#         page_tables.btn_delete_row.click()
#
#     time.sleep(2)
#     assert page_tables.no_data.exist()

#HomeWork11_1
def test_actions_with_webtables(browser):
    web_tables = Tables(browser)
    web_tables.visit()

    assert web_tables.btn_add_new_record.exist()
    web_tables.btn_add_new_record.click()
    assert web_tables.dialog_box_registration_form.exist()

    assert not web_tables.user_form.get_dom_attribute('class') == 'was-validated'
    web_tables.btn_submit.click()
    assert web_tables.user_form.get_dom_attribute('class') == 'was-validated'
    browser.refresh()

    web_tables.btn_add_new_record.click()
    web_tables.first_name.send_keys('Ksu')
    web_tables.last_name.send_keys('Filatova')
    web_tables.email.send_keys('test@test.com')
    web_tables.age.send_keys('30')
    web_tables.salary.send_keys('1000')
    web_tables.departament.send_keys('QA')
    assert web_tables.dialog_box_registration_form.exist()
    web_tables.btn_submit.click()
    time.sleep(4)
    assert not web_tables.dialog_box_registration_form.exist()

    assert web_tables.added_4th_first_name.get_text() == 'Ksu'
    assert web_tables.added_4th_last_name.get_text() == 'Filatova'
    assert web_tables.added_4th_email.get_text() == 'test@test.com'
    assert web_tables.added_4th_departament.get_text() == 'QA'
    time.sleep(4)

    web_tables.btn_edit_4th_record.click()
    assert web_tables.dialog_box_registration_form.exist()
    assert web_tables.first_name.get_dom_attribute('value') == 'Ksu'
    assert web_tables.last_name.get_dom_attribute('value') == 'Filatova'
    assert web_tables.email.get_dom_attribute('value') == 'test@test.com'
    assert web_tables.departament.get_dom_attribute('value') == 'QA'


    time.sleep(4)
    web_tables.first_name.clear()
    time.sleep(4)
    assert web_tables.first_name.get_text() == ''
    time.sleep(4)
    web_tables.first_name.send_keys('Kseniia')
    time.sleep(4)
    web_tables.btn_submit.click()
    assert web_tables.added_4th_first_name.get_text() == 'Kseniia'
    time.sleep(4)

    web_tables.btn_delete_4th_record.click()
    time.sleep(4)
    assert not web_tables.added_4th_first_name.get_text() == 'Ksu'
    assert not web_tables.added_4th_last_name.get_text() == 'Filatova'
    assert not web_tables.added_4th_email.get_text() == 'test@test.com'
    assert not web_tables.added_4th_departament.get_text() == 'QA'

    time.sleep(4)