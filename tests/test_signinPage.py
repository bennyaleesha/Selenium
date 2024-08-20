import time
import pytest
from TestData.HomePageData import HomePageData
from TestData.SigninPageData import SigninPageData
from pageObjects.SigninPage import SigninPage
from utilities.BaseClass import BaseClass


class TestSigninPage(BaseClass):
    """
    Test suite for the SignIn Page functionality.
    This suite contains tests for various sign-in scenarios and edge cases.
    """

    @pytest.mark.smoke
    def test_no_input_signin(self):
        """
        Test to verify that submitting the login form without any credentials
        returns the appropriate error messages for both email and password.
        """
        log = self.getLogger()
        signinPage = SigninPage(self.driver)

        log.info("Navigating to the Sign In Page")
        signinPage.load_signin_page()

        log.info("Clicking the login button without entering any credentials")
        signinPage.locate_login_button().click()

        log.info("Retrieving the email error message")
        email_error = signinPage.locate_email_err().text
        log.info("Retrieving the password error message")
        pass_error = signinPage.locate_pass_err().text

        log.info("Comparing the email error message to the expected message")
        assert email_error == SigninPageData.expected_email_err, " -E- Email error message is not as expected"

        log.info("Comparing the password error message to the expected message")
        assert pass_error == SigninPageData.expected_pass_err, " -E- Password error message is not as expected"

    def test_only_password(self):
        """
        Test to verify that submitting the login form with only a password
        returns an error message for the missing email.
        """
        log = self.getLogger()
        signinPage = SigninPage(self.driver)

        log.info("Refreshing the page content")
        self.driver._switch_to.default_content()

        log.info("Entering the dummy password")
        signinPage.locate_pass_tab().send_keys(SigninPageData.dummy_password)

        log.info("Clicking the login button")
        signinPage.locate_login_button().click()

        log.info("Retrieving the email error message")
        err_msg = signinPage.locate_email_err().text
        assert err_msg == SigninPageData.expected_email_err, " -E- Email error message is not as expected"

    def test_invalid_username(self, get_data):
        """
        Test to verify that submitting the login form with invalid email and password
        returns the appropriate error message for invalid email format.
        """
        log = self.getLogger()
        signinPage = SigninPage(self.driver)

        log.info("Refreshing the page content")
        self.driver.refresh()

        log.info("Entering the invalid email")
        time.sleep(2)
        signinPage.locate_email_tab().send_keys(get_data["inval_email"])

        log.info("Entering the invalid password")
        time.sleep(2)
        signinPage.locate_pass_tab().send_keys(get_data["inval_pass"])

        log.info("Clicking the login button")
        time.sleep(2)
        signinPage.locate_login_button().click()

        log.info("Retrieving the invalid email error message")
        invalid_err_msg = signinPage.locate_email_err().text
        assert invalid_err_msg == SigninPageData.expected_invalid_err, " -E- Email error message is not displayed"

    def test_password_masked(self):
        """
        Test to verify that the password field masks the password input.
        """
        log = self.getLogger()
        signinPage = SigninPage(self.driver)

        log.info("Entering the dummy password")
        signinPage.locate_pass_tab().send_keys(SigninPageData.dummy_password)

        log.info("Checking if the password is masked")
        pass_type = signinPage.locate_pass_tab().get_attribute("type")
        assert pass_type == SigninPageData.hide_pass_type, "-E- Password is not masked"

    def test_hide_button(self):
        """
        Test to verify that the show and hide buttons for the password work as expected.
        """
        log = self.getLogger()
        signinPage = SigninPage(self.driver)

        log.info("Refreshing the page content")
        self.driver.refresh()

        log.info("Entering the dummy password")
        signinPage.locate_pass_tab().send_keys(SigninPageData.dummy_password)
        time.sleep(2)

        log.info("Clicking the show button to reveal the password")
        signinPage.locate_show_button().click()

        log.info("Checking if the password is visible")
        pass_type = signinPage.locate_pass_tab().get_attribute("type")
        assert pass_type == SigninPageData.show_pass_type, "-E- Show button did not reveal the password"

        log.info("Clicking the hide button to hide the password")
        time.sleep(2)
        signinPage.locate_hide_button().click()

        log.info("Checking if the password is hidden")
        pass_type = signinPage.locate_pass_tab().get_attribute("type")
        time.sleep(2)
        assert pass_type == SigninPageData.hide_pass_type, "-E- Hide button did not conceal the password"

    def test_valid_signin(self):
        """
        Test to verify that signing in with valid credentials successfully logs the user in.
        """
        log = self.getLogger()
        signinPage = SigninPage(self.driver)

        log.info("Refreshing the page content")
        self.driver.refresh()
        time.sleep(2)

        log.info("Entering the valid email")
        signinPage.locate_email_tab().send_keys(SigninPageData.valid_email)

        log.info("Entering the valid password")
        time.sleep(2)
        signinPage.locate_pass_tab().send_keys(SigninPageData.valid_pass)

        log.info("Clicking the login button")
        time.sleep(2)
        signinPage.locate_login_button().click()

        log.info("Retrieving the user greeting message")
        time.sleep(4)
        msg_displayed = signinPage.locate_user_wish().text
        assert msg_displayed == SigninPageData.expected_msg, "-E- User greeting message is not displayed correctly"

    @pytest.fixture(params=SigninPageData.invalid_email_set)
    def get_data(self, request):
        """
        Fixture to provide test data for invalid email and password combinations.
        """
        return request.param
