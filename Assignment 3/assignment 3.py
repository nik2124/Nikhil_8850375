# Importing required libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the Amazon.ca homepage
driver.get("https://www.ebay.ca/")
time.sleep(3)

# Finding the search bar and entering text
# search_bar = driver.find_element_by_id("id","twotabsearchtextbox")
search_bar = driver.find_element("xpath","/html/body/header/table/tbody/tr/td[3]/form/table/tbody/tr/td[1]/div[1]/div/input[1]")
search_bar.send_keys("phone")

# Submitting the search query
search_bar.send_keys(Keys.RETURN)

# Waiting for the search results page to load
time.sleep(5)

# Verifying that the search results page has loaded
assert "phone" in driver.title


# opening selling page
Sell_button = driver.find_element("xpath","/html/body/div[3]/header/div[1]/ul[2]/li[2]/a")
Sell_button.click()

# Waiting for the cart to update
time.sleep(5)

#click on list item
List_item = driver.find_element("xpath","/html/body/div[2]/div[2]/main/div[1]/div/section[1]/div/div/a")
List_item.click()
# Waiting for the link page to display
time.sleep(5)

#Going to home page
Home_page = driver.find_element("xpath","/html/body/div[2]/div[1]/div/div[2]/div/header/table/tbody/tr/td[1]/a/img")
Home_page.click()
# Waiting for the link page to display
time.sleep(5)

# Closing the webdriver
driver.close()
