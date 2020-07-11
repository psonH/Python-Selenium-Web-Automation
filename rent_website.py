from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
# path to the chrome web driver
PATH = "C:/Users/Dell/Desktop/Python Selenium/driver/chromedriver.exe"
# creating the driver object
driver = webdriver.Chrome(PATH)
# accessing the website with .get() method
driver.get("https://www.99acres.com/")

# click on rent/pg tab
rent_tab = driver.find_element_by_id("ResRentTab")
rent_tab.click()
# input the location in search tab
search = driver.find_element_by_id('keyword')
search.send_keys("Pune")
search.send_keys(Keys.RETURN)
time.sleep(2)
#filter options
# bhk = driver.find_element_by_id("2")
# bhk.click()

prices = []
areas = []
bedrooms = []

flat_prices = driver.find_elements_by_id("srp_tuple_price")
for flat_price in flat_prices:
    prices.append(flat_price.text)
    print(flat_price.text)
    time.sleep(1)

print(prices)
# flat_areas = driver.find_elements_by_id("srp_tuple_primary_area")
# for flat_area in flat_areas:
#     areas.append(flat_area)
#     print(flat_area.text)
#     time.sleep(1)
#
# flat_rooms = driver.find_elements_by_id("srp_tuple_bedroom")
# for flat_room in flat_rooms:
#     bedrooms.append(flat_room)
#     print(flat_room.text)
#     time.sleep(1)