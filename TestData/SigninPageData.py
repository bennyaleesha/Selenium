class SigninPageData:
    """
    Class to hold data and constants related to the SignIn Page.
    This class provides static data used for validating different aspects of the SignIn Page.
    """

    # Expected title of the SignIn Page
    expected_page_title = "Login: Target"
    # Expected error message for missing password
    expected_pass_err = "Please enter your password"
    # Expected error message for missing email or phone number
    expected_email_err = "Please enter an email or phone number"
    # Expected error message for invalid email or phone number format
    expected_invalid_err = "Please enter a valid email or phone number"
    # Dummy password used for testing purposes
    dummy_password = "dummy@1234Pass"
    # Password input type when password is hidden
    hide_pass_type = "password"
    # Password input type when password is visible
    show_pass_type = "text"
    # Valid email used for successful sign-in
    valid_email = "bennyaleesha1234@gmail.com"
    # Valid password used for successful sign-in
    valid_pass = "Aleesha1234"
    # Expected greeting message after successful sign-in
    expected_msg = "Hi, Aleesha"
    # List of dictionaries containing invalid email and password combinations for testing
    invalid_email_set = [
        {"inval_email": "dummy1234", "inval_pass": "dummy"},
        {"inval_email": "dummy_email@email", "inval_pass": "dummy_pass"},
        {"inval_email": "dummyeamil2@.com", "inval_pass": "dummy1234"},
        {"inval_email": "123456", "inval_pass": "passunlock"},
        {"inval_email": "dummy.com", "inval_pass": "nopass"}
    ]
