from conftest import sale_page
import pytest


@pytest.mark.navigation
def test_navigate_to_women_deals_link(sale_page):
    sale_page.open_page()
    sale_page.click_to_women_deals_link()
    assert "women-sale.html" in sale_page.get_current_url()


@pytest.mark.navigation
def test_navigate_to_men_deals_link(sale_page):
    sale_page.open_page()
    sale_page.click_to_men_deals_link()
    assert "men-sale.html" in sale_page.get_current_url()

@pytest.mark.smoke
def test_sale_page_displays_product_items(sale_page):
    sale_page.open_page()
    products = sale_page.get_visible_product_items()
    assert len(products) > 0
