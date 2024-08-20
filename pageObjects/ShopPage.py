import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class ShopPage:
    """
    Page Object Model for the Shop Page of the website.
    This class provides methods to interact with elements on the Shop Page.
    """

    def __init__(self, driver):
        """
        Initializes the ShopPage object with a WebDriver instance.
        :param driver: WebDriver instance used to interact with the browser.
        """
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)  # Explicit wait with a timeout of 15 seconds

    # Locators for various elements on the Shop Page
    cart_locator = (By.XPATH, "//div[@data-test='@web/CartIcon']")
    cart_msg_locator = (By.XPATH, "//h1[@class='sc-fe064f5c-0 dtCtuk']")
    add_cart_locator = (By.XPATH, "(//button[text()='Add to cart'])[1]")
    cart_overlay_locator = (By.XPATH, "//div[@class='sc-21fc04c0-2 JduZg']")
    overlay_add_locator = (By.XPATH, "//div[@class='sc-529a2ea7-0 hbiLND']")
    checkout_overlay_locator = (By.XPATH, "//div[@class='sc-21fc04c0-2 biCmcH']")
    cart_page_locator = (By.XPATH, "//button[@data-test='cartItem-deleteBtn']")
    go_checkout_locator = (By.LINK_TEXT, "View cart & check out")
    item_locator = (By.XPATH, "//span[@class = 'sc-93ec7147-3 fUVkzh']")
    number_drop_locator = (By.XPATH, "//ul[@class='sc-5a11d645-0 fPEaaU']")
    number_locator = (By.XPATH, "//li[3]")
    cross_button_locator = (By.XPATH, "//button[@data-test='cartItem-deleteBtn']")

    def locate_cart(self):
        """
        Locates and returns the cart icon element.
        :return: WebElement for the cart icon
        """
        return self.driver.find_element(*ShopPage.cart_locator)

    def locate_cart_msg(self):
        """
        Locates and returns the message when clicked on cart.
        :return: WebElement for the cart message
        """
        return self.driver.find_element(*ShopPage.cart_msg_locator)

    def locate_add_cart(self):
        """
        Locates and returns the 'Add to cart' button element.
        :return: WebElement for the 'Add to cart' button
        """
        time.sleep(5)  # Sleep is used to wait for the element to be interactable
        add_cart = self.wait.until(EC.element_to_be_clickable(ShopPage.add_cart_locator))
        return add_cart.find_element(*ShopPage.add_cart_locator)

    def locate_overlay_add(self):
        """
        Waits for the cart overlay to be visible, then locates and returns the add to cart on overlay.
        :return: WebElement for the add overlay element
        """
        cart_overlay = self.wait.until(EC.visibility_of_element_located(ShopPage.cart_overlay_locator))
        overlay_add = cart_overlay.find_element(*ShopPage.overlay_add_locator)
        return overlay_add

    def locate_checkout(self):
        """
        Waits for the checkout overlay to be visible, then locates and returns the 'View cart & check out' button.
        :return: WebElement for the checkout button
        """
        checkout_overlay = self.wait.until(EC.visibility_of_element_located(ShopPage.checkout_overlay_locator))
        checkout_button = checkout_overlay.find_element(*ShopPage.go_checkout_locator)
        return checkout_button

    def locate_items(self):
        """
        Locates and returns the items element on the Shop Page.
        :return: WebElement for the items
        """
        return self.driver.find_element(*ShopPage.item_locator)

    def locate_number(self):
        """
        Waits for the number dropdown to be visible, then locates and returns the number element within the dropdown.
        :return: WebElement for the number element
        """
        number_drop = self.wait.until(EC.visibility_of_element_located(ShopPage.number_drop_locator))
        number = number_drop.find_element(*ShopPage.number_locator)
        return number

    def locate_del_button(self):
        """
        Waits for the delete button elements to be visible on the cart page, then returns a list of those elements.
        :return: List of WebElements for the delete buttons
        """
        self.wait.until(EC.visibility_of_element_located(ShopPage.cart_page_locator))
        cross_button_list = self.driver.find_elements(*ShopPage.cross_button_locator)
        return cross_button_list
