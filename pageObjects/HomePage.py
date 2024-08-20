from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.ShopPage import ShopPage

from TestData.HomePageData import HomePageData


class HomePage:
    """
    Page Object Model for the Home Page of the website.
    This class provides methods to interact with elements on the Home Page.
    """

    def __init__(self, driver):
        """
        Initializes the HomePage object with a WebDriver instance.
        :param driver: WebDriver instance used to interact with the browser.
        """
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10) # Explicit wait with a timeout of 10 seconds

    # Locators for various elements on the Home Page
    header_tag = (By.XPATH, "//div[@class='sc-cfda7d4b-0 fUeOuH']")
    search_tag = (By.ID, "search")
    search_button = (By.XPATH, "//button[@type='submit']")
    results_locator = (By.XPATH, "//span[@class='h-margin-r-x1']")
    navbar_content_locator = (By.XPATH, "//div[@class='sc-ab4ee1d1-4 idfyjy']")
    home_icon = (By.XPATH, "//a[@aria-label='Target home']")
    category_locator = (By.LINK_TEXT, "Categories")
    category_overlay_locator = (By.XPATH, "//div[@id='overlay-:Rjkmuqlm:']")
    school_locator = (By.XPATH, "(//span[text()='Back to School'])[2]")

    def locate_header(self):
        """
        Locates and returns the header element.
        :return: WebElement for the header
        """
        return self.driver.find_element(*HomePage.header_tag)

    def locate_search(self):
        """
        Locates and returns the search input element.
        :return: WebElement for the search input
        """
        return self.driver.find_element(*HomePage.search_tag)

    def locate_search_button(self):
        """
        Locates and returns the search button element.
        :return: WebElement for the search button
        """
        return self.driver.find_element(*HomePage.search_button)

    def locate_results(self):
        """
        Waits for the results element to be visible on the page.
        This method does not return the element but ensures it is visible.
        """
        self.wait.until(EC.visibility_of_element_located(HomePage.results_locator))

    def locate_navbar_contents(self):
        """
        Locates and returns a list of header content elements.
        :return: List of WebElements for the header contents
        """
        return self.driver.find_elements(*HomePage.navbar_content_locator)

    def locate_home_icon(self):
        """
        Locates and returns the home icon element.
        :return: WebElement for the home icon
        """
        return self.driver.find_element(*HomePage.home_icon)

    def locate_category(self):
        """
        Waits for the category button to be visible and then returns it.
        :return: WebElement for the category button
        """

        cat_button = self.wait.until(EC.visibility_of_element_located(HomePage.category_locator))
        return cat_button

    def get_school_option(self):
        """
        Waits for the category overlay to be visible, then locates and returns the back to school option within it.
        :return: WebElement for the school option
        """
        category_overlay = self.wait.until(EC.visibility_of_element_located(HomePage.category_overlay_locator))
        school_options = category_overlay.find_element(*HomePage.school_locator)
        return school_options

    def search_item(self):
        """
        Performs a search for an item using the search input and button,
        then navigates to the Shop Page.
        :return: An instance of ShopPage
        """
        self.locate_search().send_keys(HomePageData.search_item)  # Enter search term
        self.locate_search_button().click()  # Click the search button
        shopPage = ShopPage(self.driver)  # Create a ShopPage object
        return shopPage  # Return the ShopPage object for further interactions



