from selenium.webdriver.common.by import By

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.inventory_item = (By.CLASS_NAME, "inventory_item")
        self.cart_icon = (By.CLASS_NAME, "shopping_cart_badge")
        self.add_to_cart_buttons = (By.XPATH, "//button[contains(text(), 'Add to cart')]")
        self.remove_buttons = (By.XPATH, "//button[contains(text(), 'Remove')]")
        self.item_prices = (By.CLASS_NAME, "inventory_item_price")

    def get_product_count(self):
        return len(self.driver.find_elements(*self.inventory_item))

    def add_first_product_to_cart(self):
        buttons = self.driver.find_elements(*self.add_to_cart_buttons)
        if buttons:
            buttons[0].click()

    def get_cart_count(self):
        try:
            return int(self.driver.find_element(*self.cart_icon).text)
        except:
            return 0

    def get_all_prices(self):
        price_elements = self.driver.find_elements(*self.item_prices)
        return [float(p.text.replace('$', '')) for p in price_elements]
