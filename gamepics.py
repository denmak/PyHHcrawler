from selenium import webdriver
import time

from selenium.webdriver.common.keys import Keys

# http://thiagomarzagao.com/2013/11/12/webscraping-with-selenium-part-1/  go with this examples
# driver = webdriver.Chrome("/Users/denmak/Downloads/chromedriver")
# driver.get("http://www.python.org")
# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()

driver = webdriver.Chrome("/Users/denmak/Downloads/chromedriver")
url = 'https://www.lexisnexis.com/hottopics/lnacademic/?verb=sf&amp;sfi=AC00NBGenSrch'
driver.get(url)
driver.switch_to.frame("mainFrame")
driver.find_element_by_id('terms').send_keys('search')
time.sleep(3)
driver.find_element_by_id('lblAdvancDwn').click()
time.sleep(5)
driver.find_element_by_id('txtFrmDate').clear()
driver.find_element_by_id('txtFrmDate').send_keys('03/03/1983')
driver.find_element_by_id('OkButt').click()
time.sleep(3)
driver.find_element_by_id('srchButt').click()
