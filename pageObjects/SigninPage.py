import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SigninPage:
    """
    Page Object Model for the SignIn Page of the website.
    This class provides methods to interact with elements on the SignIn Page.
    """

    def __init__(self, driver):
        """
        Initializes the SigninPage object with a WebDriver instance.
        :param driver: WebDriver instance used to interact with the browser.
        """
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)  # Implicit wait with a timeout of 10 seconds

    # Locators for various elements on the Sign In Page
    signin_button_locator = (By.XPATH, "//span[text()='Sign in']")
    account_overlay_locator = (By.XPATH, "//div[@role='dialog']")
    signin_tab_locator = (By.XPATH, "//span[@class = 'sc-859e7637-0 hHZPQy']")
    login_locator = (By.ID, "login")
    email_error_locator = (By.ID, "username--ErrorMessage")
    pass_error_locator = (By.ID, "password--ErrorMessage")
    pass_tab_locator = (By.ID, "password")
    email_tab_locator = (By.ID, "username")
    show_button_locator = (By.XPATH, "//button[text()='show']")
    hide_button_locator = (By.XPATH, "//button[text()='hide']")
    user_wish_locator = (By.CSS_SELECTOR, "span[class='sc-58ad44c0-3 kwbrXj h-margin-r-x3']")

    def locate_signin_button(self):
        """
        Locates and returns the 'Sign in' button element after waiting for it to be clickable.
        :return: WebElement for the 'Sign in' button
        """
        return self.wait.until(EC.element_to_be_clickable(SigninPage.signin_button_locator))

    def locate_signin_tab(self):
        """
        Waits for the account overlay to be visible, then locates and returns the 'Sign in' tab element.
        :return: WebElement for the 'Sign in' tab
        """
        self.wait.until(EC.visibility_of_element_located(SigninPage.account_overlay_locator))
        signin_tab = self.wait.until(EC.element_to_be_clickable(SigninPage.signin_tab_locator))
        return signin_tab

    def load_signin_page(self):
        """
        Loads the Sign In page by clicking on the 'Sign in' button and then clicking on the 'Sign in' tab.

        """
        time.sleep(2)
        self.locate_signin_button().click()  # Click on the 'Sign in' button
        self.locate_signin_tab().click()  # Click on the 'Sign in' tab

    def locate_login_button(self):
        """
        Locates and returns the 'Login' button element.
        :return: WebElement for the 'Login' button
        """
        return self.driver.find_element(*SigninPage.login_locator)

    def locate_email_err(self):
        """
        Locates and returns the email error message element.
        :return: WebElement for the email error message
        """
        return self.driver.find_element(*SigninPage.email_error_locator)

    def locate_pass_err(self):
        """
        Locates and returns the password error message element.
        :return: WebElement for the password error message
        """
        return self.driver.find_element(*SigninPage.pass_error_locator)

    def locate_pass_tab(self):
        """
        Locates and returns the password input element.
        :return: WebElement for the password input
        """
        return self.driver.find_element(*SigninPage.pass_tab_locator)

    def locate_email_tab(self):
        """
        Locates and returns the email input element.
        :return: WebElement for the email input
        """
        return self.driver.find_element(*SigninPage.email_tab_locator)

    def locate_show_button(self):
        """
        Locates and returns the 'Show' button for revealing the password.
        :return: WebElement for the 'Show' button
        """
        return self.driver.find_element(*SigninPage.show_button_locator)

    def locate_hide_button(self):
        """
        Locates and returns the 'Hide' button for concealing the password.
        :return: WebElement for the 'Hide' button
        """
        return self.driver.find_element(*SigninPage.hide_button_locator)

    def locate_user_wish(self):
        """
        Locates and returns the user wish element (possibly a greeting or message).
        :return: WebElement for the user wish
        """
        return self.driver.find_element(*SigninPage.user_wish_locator)
