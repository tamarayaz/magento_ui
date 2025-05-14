import pytest
from selenium import webdriver
from pages.сreate_new_account import CreateNewAccount
from pages.sale_page import SalePage

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

