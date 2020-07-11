from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# path to the chrome web driver
PATH = "C:/Users/Dell/Desktop/Python Selenium/driver/chromedriver.exe"
# creating the driver object
driver = webdriver.Chrome(PATH)
# accessing the website with .get() method
driver.get("http://automationpractice.com/index.php")

carts = driver.find_elements_by_tag_name('a')
for cart in carts:
    if cart.get_attribute('title') == "Add to cart":
        print(cart.get_attribute('href'))
        if cart.get_attribute('href') == "http://automationpractice.com/index.php?controller=cart&add=1&id_product=4&token=e817bb0705dd58da8db074c69f729fd8":
            print("Product 4")
            #cart.click()


