from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
#path to the chrome web driver
PATH = "C:/Users/Dell/Desktop/Python Selenium/driver/chromedriver.exe"
#creating the driver object
driver = webdriver.Chrome(PATH)
#accessing the website with .get() method
driver.get("https://techwithtim.net")
print(driver.title)

search = driver.find_element_by_xpath("//*[@id='search-2']/form/label/input")
search.send_keys("text")
search.send_keys(Keys.RETURN)

#get the article titles
try:
    print("inside try")
    main_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )
    #print(main_element.text)
    articles = main_element.find_elements_by_class_name("entry-summary")
    #print(articles.text)
    for article in articles:
        # print(article)
        # header = articles.find_element_by_class_name("entry-summary")
        print(article.text)
finally:
    time.sleep(10)
    driver.quit()

