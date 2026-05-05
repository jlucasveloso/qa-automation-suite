from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class CheckoutPage(BasePage):
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BTN = (By.ID, "continue")
    FINISH_BTN = (By.ID, "finish")
    CONFIRM_HEADER = (By.CLASS_NAME, "complete-header")
    SUMMARY_TOTAL = (By.CLASS_NAME, "summary_total_label")

    def fill_info(self, first, last, postal):
        self.wait.until(EC.url_contains("checkout-step-one"))
        self.type(self.FIRST_NAME, first)
        self.type(self.LAST_NAME, last)
        self.type(self.POSTAL_CODE, postal)
        self.click(self.CONTINUE_BTN)

    def finish_purchase(self):
        self.wait.until(EC.url_contains("checkout-step-two"))
        self.click(self.FINISH_BTN)

    def get_confirmation_message(self):
        return self.get_text(self.CONFIRM_HEADER)

    def get_total(self):
        return self.get_text(self.SUMMARY_TOTAL)