from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# http://thiagomarzagao.com/2013/11/12/webscraping-with-selenium-part-1/  go with this examples 
driver = webdriver.Chrome("/Users/denmak/Downloads/chromedriver")
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()