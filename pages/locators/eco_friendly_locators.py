from selenium.webdriver.common.by import By


def size_loc(size_label):
    return (By.XPATH, f"//div[@option-label='{size_label}']")


def color_loc(color_label):
    return (By.XPATH, f"//div[@option-label='{color_label}']")


add_to_cart_btn_loc = (By.XPATH, "(//button[@title='Add to Cart'])[1]")
message_success_loc = (By.CSS_SELECTOR, ".message-success")
message_required_option_loc = (By.XPATH, "//div[text()='You need to choose options for your item.']")
product_loc = (By.CSS_SELECTOR, ".product-item.product-item")
