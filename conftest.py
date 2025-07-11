import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.create_new_account import CreateNewAccount
from pages.sale_page import SalePage
from pages.eco_friendly_page import EcoFriendlyPage
import random


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('window-size=1400,600')
    chrome_driver = webdriver.Chrome(options=options)
    return chrome_driver
    # yield chrome_driver
    # chrome_driver.save_screenshot(f'{str(random.randint(100, 10000))}.png')


@pytest.fixture()
def create_new_account(driver):
    return CreateNewAccount(driver)


@pytest.fixture()
def sale_page(driver):
    return SalePage(driver)


@pytest.fixture()
def eco_friendly_page(driver):
    return EcoFriendlyPage(driver)
