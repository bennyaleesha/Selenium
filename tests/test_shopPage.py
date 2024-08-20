import time
import pytest

from TestData.ShopPageData import ShopPageData
from pageObjects.HomePage import HomePage
from pageObjects.ShopPage import ShopPage
from utilities.BaseClass import BaseClass


class TestShopPage(BaseClass):
    """
    Test suite for the Shop Page functionality.
    This suite covers tests for cart status, adding items to the cart, and removing items from the cart.
    """

    @pytest.mark.smoke
    def test_initial_cart_status(self):
        """
        Test to validate that when the cart icon is clicked,
        the cart shows up empty if no items have been added.
        """
        log = self.getLogger()
        shopPage = ShopPage(self.driver)

        log.info("Clicking on the cart icon")
        time.sleep(2)
        shopPage.locate_cart().click()

        log.info("Verifying the cart message indicates it is empty")
        time.sleep(2)
        cart_msg = shopPage.locate_cart_msg().text
        assert cart_msg == ShopPageData.empty_cart_msg, "-E- Cart is not showing empty as expected"

    def test_adding_to_cart(self):
        """
        Test to verify if the user is able to add an item to the shopping cart
        and that the item appears in the cart.
        """
        log = self.getLogger()
        homePage = HomePage(self.driver)
        # shopPage = ShopPage(self.driver)

        log.info("Refreshing the page to ensure we start from a clean state")
        self.driver.refresh()

        log.info("Searching for the item to add to the cart")
        shopPage = homePage.search_item()

        log.info("Adding the first item to the cart")
        time.sleep(2)
        shopPage.locate_add_cart().click()

        log.info("Handling the overlay after adding the item to the cart")
        time.sleep(2)
        shopPage.locate_overlay_add().click()

        log.info("Clicking the checkout button to proceed")
        shopPage.locate_checkout().click()
        time.sleep(2)
        log.info("Refreshing the page before checking the cart")
        self.driver.refresh()

        log.info("Clicking on the cart icon to verify the added item")
        time.sleep(2)
        shopPage.locate_cart().click()

        item_count = shopPage.locate_items().text
        log.info(f"Verifying the item count in the cart: {item_count}")
        assert ShopPageData.expected_item_count in item_count, "-E- Expected item count not found in cart"

    def test_remove_cart_item(self):
        """
        Test to verify if the user can remove an item from the cart.
        """
        log = self.getLogger()
        homePage = HomePage(self.driver)
        # shopPage = ShopPage(self.driver)

        log.info("Searching for the item to add to the cart")
        shopPage = homePage.search_item()
        time.sleep(2)

        log.info("Adding the item to the cart")
        shopPage.locate_add_cart().click()
        time.sleep(2)

        add_button_text = shopPage.locate_overlay_add().text
        shopPage.locate_overlay_add().click()
        time.sleep(2)

        if add_button_text != "Add to cart":
            log.info("Item has been already added to the cart. Select the total number.")
            shopPage.locate_number().click()
            self.driver.refresh()
            time.sleep(2)
            shopPage.locate_cart().click()
        else:
            log.info("Item was successfully added to the cart. Proceeding to checkout.")
            time.sleep(2)
            shopPage.locate_checkout().click()

        log.info("Removing all items from the cart")
        button_list = shopPage.locate_del_button()
        for button in button_list:
            button.click()

        log.info("Verifying the cart is empty after removal of items")
        cart_content = shopPage.locate_cart_msg().text
        assert cart_content == ShopPageData.empty_cart_msg, "-E- Cart content is not as expected after removing items"
