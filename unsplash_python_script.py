from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
import time
import urllib.request
# path to the chrome web driver
PATH = "C:/Users/Dell/Desktop/Python Selenium/driver/chromedriver.exe"
# creating the driver object
driver = webdriver.Chrome(PATH)
# accessing the website with .get() method
driver.get("https://unsplash.com/")

# perform a search query from the search bar
search = driver.find_element_by_id('SEARCH_FORM_INPUT_nav-bar')
search.send_keys("cute cats")
search.send_keys(Keys.RETURN)
time.sleep(5)
#images_downld_tag = driver.find_elements_by_class_name("_3W4BS _1jjdS _1CBrG _1WPby xLon9 LqSCP _17avz _1B083 _3d86A")
try:
    # images_tags = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.TAG_NAME, 'a'))
    # )
    images_tags = driver.find_elements_by_tag_name('a')
    #print(images_tags)

    image_links = []
    for image_tag in images_tags:
        if image_tag.get_attribute('title') == 'Download photo':
            image_link = image_tag.get_attribute('href')
            image_links.append(image_link)
            #print(image_link)
except:
    #time.sleep(10)
    driver.quit()

driver.quit()
count = 0
for image in image_links:
    count = count + 1
    print(image)
    urllib.request.urlretrieve(image, "cat-image-" + str(count) + ".jpg")
    time.sleep(2)