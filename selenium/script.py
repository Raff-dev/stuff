from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run Chrome in headless mode

# Connect to the Selenium service using Remote
driver = webdriver.Remote(
    command_executor="http://selenium:4444/wd/hub",  # URL of the Selenium service
    options=options,
)

driver.get("https://www.google.com")
print(driver.page_source)

driver.quit()
