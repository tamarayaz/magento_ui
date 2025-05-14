from pages.base_page import BasePage
from pages.locators import  sale_page_locators as loc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SalePage(BasePage):
    page_url = "/sale.html"


    def click_to_women_deals_link(self):
        self.find(loc.womens_deals_link).click()


    def click_to_men_deals_link(self):
        self.find(loc.mens_bargains_link).click()

    def get_visible_product_items(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(loc.product_items_loc)
        )
        return self.find_all(loc.product_items_loc)
