from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class CartPage(BasePage):
    ITEMS = (By.CLASS_NAME, "cart_item")
    CHECKOUT_BTN = (By.ID, "checkout")

    def get_item_count(self):
        try:
            self.wait.until(EC.presence_of_element_located(self.ITEMS))
            return len(self.driver.find_elements(*self.ITEMS))
        except Exception:
            return 0

    def proceed_to_checkout(self):
        self.click(self.CHECKOUT_BTN)