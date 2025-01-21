from pages.text_box import TextBox


def test_text_box(browser):

    text_box_page = TextBox(browser)

    text_box_page.visit()
    text_box_page.name.send_keys('Ksu')
    text_box_page.current_address.send_keys('street')
    text_box_page.btn_submit.click()

    assert text_box_page.output_name.get_text() == 'Name: Ksu'
    assert text_box_page.output_current_address.get_text() == 'Current Address: street'