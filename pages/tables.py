from pages.base_page import BasePage
from components.components import WebElement


class Tables(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables'

        super().__init__(driver, self.base_url)

        self.btn_delete_row = WebElement(driver, '//span[@title="Delete"]', 'xpath')
        self.no_data = WebElement(driver, 'div.rt-noData')

        self.dialog_box_registration_form = WebElement(driver, 'body > div.fade.modal.show > div > div')
        self.user_form = WebElement(driver, '#userForm')
        self.first_name = WebElement(driver, '#firstName')
        self.last_name = WebElement(driver, '#lastName')
        self.email = WebElement(driver, '#userEmail')
        self.age = WebElement(driver, '#age')
        self.salary = WebElement(driver, '#salary')
        self.departament = WebElement(driver, '#department')
        self.btn_submit = WebElement(driver, '#submit')
        self.btn_add_new_record = WebElement(driver, '#addNewRecordButton')
        self.added_4th_first_name = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-tbody > div:nth-child(4) > div > div:nth-child(1)')
        self.added_4th_last_name = WebElement(driver,'#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-tbody > div:nth-child(4) > div > div:nth-child(2)')
        self.added_4th_email = WebElement(driver,'#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-tbody > div:nth-child(4) > div > div:nth-child(4)')
        self.added_4th_departament = WebElement(driver,'#app > div > div > div > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-tbody > div:nth-child(4) > div > div:nth-child(6)')
        self.btn_edit_4th_record = WebElement(driver, '#edit-record-4 > svg')
        self.btn_delete_4th_record = WebElement(driver, '#delete-record-4 > svg')

        self.header_first_name = WebElement(driver, 'div.rt-th:nth-child(1)')
        self.header_last_name = WebElement(driver, 'div.rt-th:nth-child(2)')
        self.header_email = WebElement(driver, 'div.rt-th:nth-child(3)')
        self.header_age = WebElement(driver, 'div.rt-th:nth-child(4)')
        self.header_salary = WebElement(driver, 'div.rt-th:nth-child(5)')
        self.header_department = WebElement(driver, 'div.rt-th:nth-child(6)')
        self.header_action = WebElement(driver, 'div.rt-th:nth-child(7)')
