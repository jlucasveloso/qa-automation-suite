from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

VALID_USER = "standard_user"
VALID_PASS = "secret_sauce"


class TestE2EPurchaseFlow:
    def test_login_success(self, driver):
        login = LoginPage(driver)
        login.open_login()
        login.login(VALID_USER, VALID_PASS)

        inventory = InventoryPage(driver)
        assert inventory.get_title() == "Products"

    def test_login_invalid_credentials(self, driver):
        login = LoginPage(driver)
        login.open_login()
        login.login("wrong_user", "wrong_pass")
        assert "Username and password do not match" in login.get_error_message()

    def test_add_single_product_to_cart(self, driver):
        login = LoginPage(driver)
        login.open_login()
        login.login(VALID_USER, VALID_PASS)

        inventory = InventoryPage(driver)
        inventory.add_product_by_index(0)
        assert inventory.get_cart_count() == 1

    def test_add_multiple_products_to_cart(self, driver):
        login = LoginPage(driver)
        login.open_login()
        login.login(VALID_USER, VALID_PASS)

        inventory = InventoryPage(driver)
        inventory.add_product_by_index(0)
        inventory.add_product_by_index(1)
        assert inventory.get_cart_count() == 2

    def test_complete_purchase_flow(self, driver):
        login = LoginPage(driver)
        login.open_login()
        login.login(VALID_USER, VALID_PASS)

        inventory = InventoryPage(driver)
        inventory.add_product_by_index(0)
        inventory.add_product_by_index(1)
        assert inventory.get_cart_count() == 2
        inventory.go_to_cart()

        cart = CartPage(driver)
        cart.proceed_to_checkout()

        checkout = CheckoutPage(driver)
        checkout.fill_info("QA", "Tester", "12345")
        assert "Total:" in checkout.get_total()
        checkout.finish_purchase()

        assert checkout.get_confirmation_message() == "Thank you for your order!"