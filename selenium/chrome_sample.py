# chromedriver install: https://sites.google.com/a/chromium.org/chromedriver/downloads
from selenium import webdriver

# windowsの場合
# chromedriver_path = '../node_modules/chromedriver/lib/chromedriver/chromedriver'
# macの場合
chromedriver_path = '../node_modules/chromedriver/bin/chromedriver'

driver = webdriver.Chrome(executable_path=chromedriver_path)
driver.get("http://www.python.org")
driver.quit()
