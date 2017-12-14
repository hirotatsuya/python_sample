# chromedriver install: https://sites.google.com/a/chromium.org/chromedriver/downloads
from selenium import webdriver

# chromedriver_path = './node_modules/chromedriver/bin/chromedriver'
# chromedriver_path = './chromedriver'
chromedriver_path = '../node_modules/chromedriver/lib/chromedriver/chromedriver'
driver = webdriver.Chrome(executable_path=chromedriver_path)
driver.get("http://www.python.org")
driver.quit()