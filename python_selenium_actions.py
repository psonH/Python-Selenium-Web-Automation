from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# path to the chrome web driver
PATH = "C:/Users/Dell/Desktop/Python Selenium/driver/chromedriver.exe"
# creating the driver object
driver = webdriver.Chrome(PATH)
# accessing the website with .get() method
driver.get("https://techwithtim.net")

# navigating to a page by clicking a link
link = driver.find_element_by_link_text("Python Programming")
link.click()
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Beginner Python Tutorials"))
    )
    element.click()
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "sow-button-19310003"))
    )
    # click the click-able elements
    element.click()
    # go back to the previous page
    driver.back()
except:
    #time.sleep(10)
    driver.quit()