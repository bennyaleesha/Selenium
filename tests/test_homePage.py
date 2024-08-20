import time
import pytest
from TestData.HomePageData import HomePageData
from TestData.SigninPageData import SigninPageData
from pageObjects.HomePage import HomePage
from pageObjects.SigninPage import SigninPage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):
    """
    Test suite for verifying functionality on the Home Page.
    Includes tests for page load, search functionality, navigation items, category selection, and sign-in navigation.
    """

    @pytest.mark.smoke
    def test_homepage_load(self):
        """
        Test to ensure the home page loads correctly with the expected title and header.
        """
        log = self.getLogger()
        homePage = HomePage(self.driver)

        log.info("Verifying the page title")
        assert HomePageData.homePageTitle in self.driver.title, "-E- Title is not as expected"

        log.info("Locating and verifying the header presence")
        header = homePage.locate_header()
        assert header, "-E- Header not found"

    def test_search_button(self):
        """
        Test to check if the user can search for an item using the search bar and search button.
        """
        log = self.getLogger()
        homePage = HomePage(self.driver)

        log.info("Performing a search for an item")
        homePage.search_item()
        time.sleep(2)

        log.info("Waiting for search results to be visible")
        homePage.locate_results()

        log.info("Verifying search result presence in the page source")
        assert HomePageData.search_result in self.driver.page_source, "-E- Search result not found in page source"

    def test_nav_items(self):
        """
        Test to validate if all required sections are present in the top navigation bar.
        """
        log = self.getLogger()
        homePage = HomePage(self.driver)

        log.info("Retrieving navbar contents for validation")
        content_list = []
        navbar_content = homePage.locate_navbar_contents()
        for content in navbar_content:
            content_list.append(content.text)

        log.info(f"Navbar content found: {content_list}")
        assert content_list == HomePageData.expected_header_content, "-E- Navigation items do not match expected content"

    def test_category_options(self):
        """
        Test to validate if a desired category can be selected from the category dropdown.
        """
        log = self.getLogger()
        homePage = HomePage(self.driver)

        log.info("Navigating to the category dropdown")
        homePage.locate_home_icon().click()
        time.sleep(2)

        log.info("Selecting the category dropdown")
        homePage.locate_category().click()
        time.sleep(2)

        log.info("Selecting the 'Back to School' option from the dropdown")
        homePage.get_school_option().click()

        log.info("Verifying if the 'Back to School' content is present on the page")
        assert HomePageData.school_content in self.driver.page_source, "-E- 'Back to School' content not found in page source"

    def test_signin_button(self):
        """
        Test to validate if the sign-in button navigates the user to the sign-in page.
        """
        log = self.getLogger()
        signinPage = SigninPage(self.driver)

        log.info("Navigating to the sign-in page")
        signinPage.load_signin_page()
        time.sleep(2)

        log.info("Verifying the page title of the sign-in page")
        page_title = self.driver.title
        assert page_title == SigninPageData.expected_page_title, "-E- Page title is not as expected"
