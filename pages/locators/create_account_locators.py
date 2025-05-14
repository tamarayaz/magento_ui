from selenium.webdriver.common.by import By


firstname_field_loc = (By.ID, "firstname")
lastname_field_loc = (By.ID, "lastname")
email_field_loc = (By.ID, "email_address")
password_field_loc = (By.ID, "password")
confirm_password_field_loc = (By.ID, "password-confirmation")
btn_create_account_loc = (By.XPATH, "//button[@title='Create an Account']")
success_message_loc = (By.XPATH, "//div[@data-ui-id='message-success']")
error_required_field_message_loc = (By.CSS_SELECTOR, ".mage-error")
password_confirmation_error_loc = (By.XPATH, "//div[text()='Please enter the same value again.']")
