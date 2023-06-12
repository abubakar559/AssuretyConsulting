import selenium
from selenium import webdriver

# Check Selenium version
print("Selenium version:", selenium.__version__)

# Check WebDriver version for Chrome
print("ChromeDriver version:", webdriver.Chrome().capabilities['chrome']['chromedriverVersion'])

# Check WebDriver version for Firefox
print("GeckoDriver version:", webdriver.Firefox().capabilities['moz:geckodriverVersion'])

# Check WebDriver version for other browsers
# Replace "browser_name" with the appropriate browser name (e.g., "edge", "safari", "opera")
print("WebDriver version for other browsers:", webdriver.__version__)
