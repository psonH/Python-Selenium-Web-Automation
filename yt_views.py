from selenium import webdriver
from selenium.webdriver.common.keys import Keys

PATH = "C:/Users/Dell/Desktop/Python Selenium/driver/chromedriver.exe"
# creating the driver object
driver = webdriver.Chrome(PATH)
# accessing the website with .get() method
driver.get("https://www.quora.com/Does-YouTube-count-my-views-if-I-do-not-log-in-my-account")

# search = driver.find_element_by_tag_name('input')
# search.send_keys("Priyank Hajela")
# search.send_keys(Keys.RETURN)
#
# video_links = driver.find_elements_by_tag_name('a')
# for video_link in video_links:
#     print(video_link.get_attribute('href'))
#     if video_link.get_attribute('href') == "https://www.youtube.com/watch?v=A-iQ1wRwZD0":
#         print("Video Found")
#         video_link.click()