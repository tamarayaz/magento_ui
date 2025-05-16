from pages.base_page import BasePage
from pages.locators import eco_friendly_locators as loc
from pages.locators.eco_friendly_locators import size_loc, color_loc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class EcoFriendlyPage(BasePage):
    page_url = "/collections/eco-friendly.html"

    def select_size_option(self, size_label):
        self.find(size_loc(size_label)).click()

    def select_color_option(self, color_label):
        self.find(color_loc(color_label)).click()

    def click_add_to_cart(self):
        self.find(loc.add_to_cart_btn_loc).click()

    def check_add_to_cart_success_message(self, expected_text):
        message = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(loc.message_success_loc)
        )
        actual_text = message.text.strip()
        assert expected_text in actual_text

    def check_required_option_message(self, expected_message):
        message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(loc.message_required_option_loc)
        )
        actual_text = message.text
        assert expected_message in actual_text

    def hover_over_product(self):
        product = self.find(loc.product_loc)
        ActionChains(self.driver).move_to_element(product).perform()
