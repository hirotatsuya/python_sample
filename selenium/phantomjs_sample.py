# phantomjs install: http://phantomjs.org/download.html
from selenium import webdriver
from bs4 import BeautifulSoup
import re
import lxml

driver = webdriver.PhantomJS(executable_path='./phantomjs')
driver.get("https://coincheck.com/ja/exchange")
source = driver.page_source
ripple = BeautifulSoup(source, 'lxml').find_all(class_=re.compile('currency_desc ng-binding'))[7].text
print(ripple)
driver.quit()


