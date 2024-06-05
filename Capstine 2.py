from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the Chrome driver
driver = webdriver.Chrome()

# Test Case 1: Forgot Password link validation on login page
def test_forgot_password():
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    wait = WebDriverWait(driver, 10)

    # Click on Forgot Password link using XPath
    forgot_password_link = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[4]/p')))
    forgot_password_link.click()

    # Ensure the username textbox is visible
    username_textbox = wait.until(EC.visibility_of_element_located((By.ID, "securityAuthentication_userName")))
    assert username_textbox.is_displayed(), "Username textbox is not visible"

    # Provide username and click on Reset Password using XPath
    username_textbox.send_keys("Admin")
    reset_button = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/div/form/div[2]/button[2]')
    reset_button.click()

    # Validate the success message
    success_message = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.message")))
    assert "Reset Password link sent successfully" in success_message.text, "Success message not found"

# Test Case 2: Header Validation on Admin Page
def test_admin_page_headers():
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    wait = WebDriverWait(driver, 10)

    # Login as Admin using ID for username and password field
    username = wait.until(EC.visibility_of_element_located((By.ID, "txtUsername")))
    password = driver.find_element(By.ID, "txtPassword")
    login_button = driver.find_element(By.ID, "btnLogin")

    username.send_keys("Admin")
    password.send_keys("admin123")
    login_button.click()

    # Navigate to Admin page
    admin_tab = wait.until(EC.element_to_be_clickable((By.ID, "menu_admin_viewAdminModule")))
    admin_tab.click()

    # Validate page title
    page_title = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "h1")))
    assert page_title.text == "System Users", "Admin page title is incorrect"

    # Validate presence of headers
    expected_headers = ["User Management", "Job", "Organization", "Qualifications", "Nationalities", "Corporate Banking", "Configuration"]
    for header in expected_headers:
        header_element = driver.find_element(By.XPATH, f"//a[text()='{header}']")
        assert header_element.is_displayed(), f"{header} header is not visible"

# Test Case 3: Main Menu Validation on Admin Page
def test_admin_page_menu():
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    wait = WebDriverWait(driver, 10)

    # Login as Admin using ID for username and password field
    username = wait.until(EC.visibility_of_element_located((By.ID, "txtUsername")))
    password = driver.find_element(By.ID, "txtPassword")
    login_button = driver.find_element(By.ID, "btnLogin")

    username.send_keys("Admin")
    password.send_keys("admin123")
    login_button.click()

    # Navigate to Admin page
    admin_tab = wait.until(EC.element_to_be_clickable((By.ID, "menu_admin_viewAdminModule")))
    admin_tab.click()

    # Validate presence of menu items
    expected_menus = ["Admin", "PIM", "Leave", "Time", "Recruitment", "My Info", "Performance", "Dashboard", "Directory", "Maintenance", "Buzz"]
    for menu in expected_menus:
        menu_element = driver.find_element(By.XPATH, f"//b[text()='{menu}']")
        assert menu_element.is_displayed(), f"{menu} menu item is not visible"

# Run test cases
try:
    test_forgot_password()
    print("Test Case 1: Forgot Password link validation passed.")
    test_admin_page_headers()
    print("Test Case 2: Header Validation on Admin Page passed.")
    test_admin_page_menu()
    print("Test Case 3: Main Menu Validation on Admin Page passed.")
finally:
    driver.quit()
