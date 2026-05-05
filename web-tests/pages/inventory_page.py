from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class InventoryPage(BasePage):
    TITLE = (By.CLASS_NAME, "title")
    ADD_BTN = (By.CSS_SELECTOR, ".btn_inventory")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def get_title(self):
        return self.get_text(self.TITLE)

    def add_product_by_index(self, index=0):
        buttons = self.wait.until(
            EC.presence_of_all_elements_located(self.ADD_BTN)
        )
        buttons[index].click()

    def get_cart_count(self):
        try:
            return int(self.get_text(self.CART_BADGE))
        except Exception:
            return 0

    def go_to_cart(self):
        self.click(self.CART_LINK)