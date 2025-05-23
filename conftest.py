import pytest
from selenium import webdriver
from pages.create_new_account import CreateNewAccount
from pages.sale_page import SalePage
from pages.eco_friendly_page import EcoFriendlyPage


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    return chrome_driver


@pytest.fixture()
def create_new_account(driver):
    return CreateNewAccount(driver)


@pytest.fixture()
def sale_page(driver):
    return SalePage(driver)


@pytest.fixture()
def eco_friendly_page(driver):
    return EcoFriendlyPage(driver)
