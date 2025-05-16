from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.locators import create_account_locators as loc


class CreateNewAccount(BasePage):
    page_url = "/customer/account/create/"

    def fill_all_required_fields(self, data):
        first_name_field = self.find(loc.firstname_field_loc)
        last_name_field = self.find(loc.lastname_field_loc)
        email_field = self.find(loc.email_field_loc)
        password_field = self.find(loc.password_field_loc)
        confirm_password_field = self.find(loc.confirm_password_field_loc)

        first_name_field.send_keys(data.first_name)
        last_name_field.send_keys(data.last_name)
        email_field.send_keys(data.email)
        password_field.send_keys(data.password)
        confirm_password_field.send_keys(data.confirm_password)

        create_account_button = self.find(loc.btn_create_account_loc)
        create_account_button.click()

    def check_message_of_successful_registration_is(self, text):
        success_message_element = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(loc.success_message_loc)
        )
        success_text = success_message_element.text
        assert success_text in text

    def click_create_account_button(self):
        self.find(loc.btn_create_account_loc).click()

    def check_required_field_errors_displayed(self, expected_messages):
        errors = self.find_all(loc.error_required_field_message_loc)
        actual_messages = [error.text for error in errors if error.is_displayed()]
        for expected in expected_messages:
            assert expected in actual_messages

    def check_password_mismatch_error_displayed(self, expected_message):
        error = self.find(loc.password_confirmation_error_loc)

        assert error.text == expected_message
